from enum import Enum
from ecommerce.notificacao import Notificacao, NotificacaoEmail, NotificacaoSMS


class CanalNotificacao(Enum):
    EMAIL = "email"
    SMS = "sms"


class CriadorNotificacao:
    def criar(self, canal: CanalNotificacao) -> Notificacao:
        if canal == CanalNotificacao.EMAIL:
            return NotificacaoEmail()
        if canal == CanalNotificacao.SMS:
            return NotificacaoSMS()
        raise ValueError(f"Canal de notificação inválido: {canal}")
