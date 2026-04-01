import random
import time
import requests
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from core.monitoring.logger import setup_logger

class BaseScraper(ABC):
    """
    Clase base para todos los scrapers del sistema.
    Maneja sesiones, proxies, user-agents y control de velocidad.
    """
    
    def __init__(self, name: str, respect_robots: bool = True):
        self.name = name
        self.logger = setup_logger(name)
        self.session = requests.Session()
        self.respect_robots = respect_robots
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
        ]

    def get_random_ua(self) -> str:
        return random.choice(self.user_agents)

    def fetch(self, url: str, params: Optional[Dict[str, Any]] = None, use_proxy: bool = False) -> Optional[requests.Response]:
        """
        Realiza una petición HTTP con manejo de errores y reintentos.
        """
        headers = {"User-Agent": self.get_random_ua()}
        proxies = self._get_proxies() if use_proxy else None
        
        try:
            self.logger.info(f"Fetching URL: {url}")
            # Respetar rate limit (ejemplo: 1-3 segundos)
            time.sleep(random.uniform(1, 3))
            
            response = self.session.get(url, headers=headers, params=params, proxies=proxies, timeout=15)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"HTTP Error for {url}: {e}")
        except Exception as e:
            self.logger.error(f"Unexpected error for {url}: {e}")
        
        return None

    def _get_proxies(self) -> Dict[str, str]:
        # Aquí se integraría con un servicio de proxies (tipo Bright Data, ProxyRack, etc.)
        # Por ahora retorna un placeholder
        return {}

    @abstractmethod
    def run(self):
        """Método principal a implementar por cada scraper."""
        pass
