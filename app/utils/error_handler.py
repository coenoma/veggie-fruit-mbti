from enum import Enum
import logging

# ログレベルの定義
class LogLevel(Enum):
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

# エラー種別の定義
class ErrorType(Enum):
    VALIDATION_ERROR = "入力値が不正です"
    DATABASE_ERROR = "データベースエラーが発生しました"
    NETWORK_ERROR = "ネットワークエラーが発生しました"
    AUTH_ERROR = "認証エラーが発生しました"
    NOT_FOUND = "リソースが見つかりません"
    SERVER_ERROR = "サーバーエラーが発生しました"

# エラーメッセージの形式
class ErrorResponse:
    def __init__(self, error_type: ErrorType, message: str = None, details: dict = None):
        self.error_type = error_type
        self.message = message or error_type.value
        self.details = details or {}

    def to_dict(self):
        return {
            'error': self.error_type.name,
            'message': self.message,
            'details': self.details
        }

# ログ出力の設定
def setup_logging():
    logging.basicConfig(
        level=LogLevel.INFO.value,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('app.log')
        ]
    )
