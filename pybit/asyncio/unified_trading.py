from dataclasses import dataclass
from ._v5_misc import MiscHTTP
from ._v5_market import MarketHTTP
from ._v5_trade import TradeHTTP
from ._v5_account import AccountHTTP
from ._v5_asset import AssetHTTP
from ._v5_position import PositionHTTP
from ._v5_pre_upgrade import PreUpgradeHTTP
from ._v5_spot_leverage_token import SpotLeverageHTTP
from ._v5_spot_margin_trade import SpotMarginTradeHTTP
from ._v5_user import UserHTTP
from ._v5_broker import BrokerHTTP
from ._v5_institutional_loan import InstitutionalLoanHTTP


WSS_NAME = "Unified V5"
PRIVATE_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.com/v5/private"
PUBLIC_WSS = "wss://{SUBDOMAIN}.{DOMAIN}.com/v5/public/{CHANNEL_TYPE}"
AVAILABLE_CHANNEL_TYPES = [
    "inverse",
    "linear",
    "spot",
    "option",
    "private",
]

@dataclass
class HTTP(
    MiscHTTP,
    MarketHTTP,
    TradeHTTP,
    AccountHTTP,
    AssetHTTP,
    PositionHTTP,
    PreUpgradeHTTP,
    SpotLeverageHTTP,
    SpotMarginTradeHTTP,
    UserHTTP,
    BrokerHTTP,
    InstitutionalLoanHTTP,
):
    def __init__(self, **args):
        super().__init__(**args)