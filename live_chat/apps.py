from django.apps import AppConfig


class LiveChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'live_chat'
    
    def ready(self):
        import rag.rag_singleton