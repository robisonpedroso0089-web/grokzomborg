"""
😂 GROKZOMBORG - Random Joke Generator
ROOOAAAR! Gerador de piadas aleatórias usando APIs externas

Integra com múltiplas APIs de piadas:
- JokeAPI (https://jokeapi.dev)
- Official Joke API (https://official-joke-api.appspot.com)
- Dad Jokes API (https://icanhazdadjoke.com)
"""

import requests
import json
from typing import Dict, List, Optional, Tuple
from enum import Enum
import random


class JokeCategory(Enum):
    """Categorias de piadas disponíveis"""
    GENERAL = "general"
    PROGRAMMING = "programming"
    KNOCK_KNOCK = "knock-knock"
    ALL = "any"


class JokeType(Enum):
    """Tipos de piadas"""
    SINGLE = "single"
    TWOPART = "twopart"


class JokeGenerator:
    """Gerador de piadas usando APIs externas"""
    
    # APIs disponíveis
    JOKE_API_URL = "https://jokeapi.dev/random"
    OFFICIAL_JOKE_API = "https://official-joke-api.appspot.com/random_joke"
    DAD_JOKE_API = "https://icanhazdadjoke.com"
    
    def __init__(self, timeout: int = 5):
        """
        Inicializa o gerador de piadas
        
        Args:
            timeout: Tempo máximo de espera por resposta (segundos)
        """
        self.timeout = timeout
        self.joke_history = []
        self.max_history = 50
    
    def get_random_joke_from_jokeapi(
        self,
        category: JokeCategory = JokeCategory.ALL,
        joke_type: Optional[str] = None
    ) -> Optional[Dict]:
        """
        Obtém uma piada aleatória da JokeAPI
        
        Args:
            category: Categoria de piada
            joke_type: Tipo de piada (single ou twopart)
        
        Returns:
            Dicionário com a piada ou None se falhar
        """
        try:
            params = {
                'category': category.value,
                'type': joke_type if joke_type else 'single'
            }
            
            response = requests.get(
                self.JOKE_API_URL,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('error'):
                print(f"❌ Erro da API: {data.get('message')}")
                return None
            
            joke = {
                'source': 'JokeAPI',
                'category': data.get('category'),
                'type': data.get('type')
            }
            
            if data.get('type') == 'single':
                joke['joke'] = data.get('joke')
            else:
                joke['setup'] = data.get('setup')
                joke['delivery'] = data.get('delivery')
            
            self._add_to_history(joke)
            return joke
        
        except requests.RequestException as e:
            print(f"❌ Erro ao conectar com JokeAPI: {e}")
            return None
    
    def get_random_joke_from_official(self) -> Optional[Dict]:
        """
        Obtém uma piada aleatória da Official Joke API
        
        Returns:
            Dicionário com a piada ou None se falhar
        """
        try:
            response = requests.get(
                self.OFFICIAL_JOKE_API,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            
            joke = {
                'source': 'Official Joke API',
                'setup': data.get('setup'),
                'delivery': data.get('delivery'),
                'type': 'twopart',
                'id': data.get('id')
            }
            
            self._add_to_history(joke)
            return joke
        
        except requests.RequestException as e:
            print(f"❌ Erro ao conectar com Official Joke API: {e}")
            return None
    
    def get_random_dad_joke(self) -> Optional[Dict]:
        """
        Obtém uma piada de pai da Dad Jokes API
        
        Returns:
            Dicionário com a piada ou None se falhar
        """
        try:
            headers = {'Accept': 'application/json'}
            response = requests.get(
                self.DAD_JOKE_API,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            data = response.json()
            
            joke = {
                'source': 'Dad Jokes API',
                'joke': data.get('joke'),
                'type': 'single',
                'id': data.get('id')
            }
            
            self._add_to_history(joke)
            return joke
        
        except requests.RequestException as e:
            print(f"❌ Erro ao conectar com Dad Jokes API: {e}")
            return None
    
    def get_random_joke(self) -> Optional[Dict]:
        """
        Obtém uma piada aleatória de qualquer API
        
        Returns:
            Dicionário com a piada ou None se falhar
        """
        apis = [
            self.get_random_joke_from_jokeapi,
            self.get_random_joke_from_official,
            self.get_random_dad_joke
        ]
        
        # Embaralha as APIs
        random.shuffle(apis)
        
        for api in apis:
            joke = api()
            if joke:
                return joke
        
        print("❌ Falha ao obter piada de todas as APIs")
        return None
    
    def get_programming_joke(self) -> Optional[Dict]:
        """
        Obtém uma piada sobre programação
        
        Returns:
            Dicionário com a piada ou None se falhar
        """
        return self.get_random_joke_from_jokeapi(
            category=JokeCategory.PROGRAMMING
        )
    
    def get_knock_knock_joke(self) -> Optional[Dict]:
        """
        Obtém uma piada "Knock Knock"
        
        Returns:
            Dicionário com a piada ou None se falhar
        """
        return self.get_random_joke_from_jokeapi(
            category=JokeCategory.KNOCK_KNOCK
        )
    
    def _add_to_history(self, joke: Dict) -> None:
        """Adiciona piada ao histórico"""
        self.joke_history.append(joke)
        
        # Limitar tamanho do histórico
        if len(self.joke_history) > self.max_history:
            self.joke_history.pop(0)
    
    def get_history(self) -> List[Dict]:
        """Retorna histórico de piadas"""
        return self.joke_history.copy()
    
    def clear_history(self) -> None:
        """Limpa o histórico"""
        self.joke_history.clear()
        print("🧹 Histórico de piadas limpo")
    
    def print_joke(self, joke: Dict) -> None:
        """
        Imprime uma piada formatada
        
        Args:
            joke: Dicionário com a piada
        """
        if not joke:
            print("❌ Piada não disponível")
            return
        
        print("\n" + "="*60)
        print(f"📚 Fonte: {joke.get('source', 'Desconhecida')}")
        
        if joke.get('type') == 'single':
            print(f"\n😂 {joke.get('joke', '')}")
        else:
            print(f"\n🤔 {joke.get('setup', '')}")
            print(f"😂 {joke.get('delivery', '')}")
        
        if joke.get('category'):
            print(f"\n📁 Categoria: {joke.get('category')}")
        
        print("="*60 + "\n")
    
    def save_favorites(self, filename: str = 'favorite_jokes.json') -> None:
        """
        Salva piadas favoritas em arquivo
        
        Args:
            filename: Nome do arquivo
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.joke_history, f, ensure_ascii=False, indent=2)
            print(f"💾 {len(self.joke_history)} piadas salvas em {filename}")
        except IOError as e:
            print(f"❌ Erro ao salvar piadas: {e}")
    
    def load_favorites(self, filename: str = 'favorite_jokes.json') -> None:
        """
        Carrega piadas favoritas de arquivo
        
        Args:
            filename: Nome do arquivo
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.joke_history = json.load(f)
            print(f"📂 {len(self.joke_history)} piadas carregadas de {filename}")
        except FileNotFoundError:
            print(f"⚠️ Arquivo não encontrado: {filename}")
        except json.JSONDecodeError:
            print(f"❌ Erro ao decodificar arquivo JSON")


class JokeBot:
    """Bot interativo de piadas"""
    
    def __init__(self):
        """Inicializa o bot de piadas"""
        self.generator = JokeGenerator()
        self.running = True
    
    def display_menu(self) -> None:
        """Mostra o menu de opções"""
        print("\n" + "="*60)
        print("🎭 GROKZOMBORG - Gerador de Piadas")
        print("="*60)
        print("\n1️⃣  Piada aleatória")
        print("2️⃣  Piada de programação")
        print("3️⃣  Piada 'Knock Knock'")
        print("4️⃣  Ver histórico")
        print("5️⃣  Salvar favoritas")
        print("6️⃣  Carregar favoritas")
        print("7️⃣  Limpar histórico")
        print("8️⃣  Sair")
        print("\n" + "="*60)
    
    def run(self) -> None:
        """Executa o bot interativo"""
        print("\n🚀 Iniciando Gerador de Piadas...")
        print("🌍 Conectando com APIs externas...")
        
        while self.running:
            self.display_menu()
            choice = input("\n👉 Escolha uma opção (1-8): ").strip()
            
            if choice == '1':
                print("\n⏳ Obtendo piada aleatória...")
                joke = self.generator.get_random_joke()
                self.generator.print_joke(joke)
            
            elif choice == '2':
                print("\n⏳ Obtendo piada de programação...")
                joke = self.generator.get_programming_joke()
                self.generator.print_joke(joke)
            
            elif choice == '3':
                print("\n⏳ Obtendo piada Knock Knock...")
                joke = self.generator.get_knock_knock_joke()
                self.generator.print_joke(joke)
            
            elif choice == '4':
                self._show_history()
            
            elif choice == '5':
                filename = input("📝 Nome do arquivo (default: favorite_jokes.json): ").strip()
                if not filename:
                    filename = 'favorite_jokes.json'
                self.generator.save_favorites(filename)
            
            elif choice == '6':
                filename = input("📝 Nome do arquivo (default: favorite_jokes.json): ").strip()
                if not filename:
                    filename = 'favorite_jokes.json'
                self.generator.load_favorites(filename)
            
            elif choice == '7':
                confirm = input("⚠️  Tem certeza? (s/n): ").strip().lower()
                if confirm == 's':
                    self.generator.clear_history()
            
            elif choice == '8':
                print("\n👋 Até logo! ROOOAAAR-ZIIIMB!!!!")
                self.running = False
            
            else:
                print("\n❌ Opção inválida! Tente novamente.")
    
    def _show_history(self) -> None:
        """Mostra o histórico de piadas"""
        history = self.generator.get_history()
        
        if not history:
            print("\n📭 Nenhuma piada no histórico")
            return
        
        print(f"\n📚 Histórico ({len(history)} piadas):")
        print("="*60)
        
        for i, joke in enumerate(history, 1):
            print(f"\n{i}. {joke.get('source')}")
            
            if joke.get('type') == 'single':
                print(f"   {joke.get('joke', '')[:80]}...")
            else:
                print(f"   {joke.get('setup', '')[:80]}...")
        
        print("\n" + "="*60)


if __name__ == '__main__':
    print("\n🎭 GROKZOMBORG - Gerador de Piadas Aleatórias")
    print("ROOOAAAR! Prepare-se para rir!\n")
    
    # Teste da classe
    generator = JokeGenerator()
    
    # Obter uma piada aleatória
    print("📥 Obtendo piada aleatória...")
    joke = generator.get_random_joke()
    generator.print_joke(joke)
    
    # Obter piada de programação
    print("💻 Obtendo piada de programação...")
    prog_joke = generator.get_programming_joke()
    generator.print_joke(prog_joke)
    
    # Obter piada de pai
    print("👨 Obtendo piada de pai...")
    dad_joke = generator.get_random_dad_joke()
    generator.print_joke(dad_joke)
    
    # Mostrar histórico
    print(f"\n📊 Total de piadas no histórico: {len(generator.get_history())}")
    
    # Bot interativo (descomente para usar)
    # bot = JokeBot()
    # bot.run()
