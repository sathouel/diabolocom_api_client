from diabolocom_api_client.utils import urljoin
from . import base
from .campaigns import CampaignsPool, CampaignsV2Pool


class AccountWrapupsPool(
    base.ResourcePool,
    base.GettableResource,
    base.ListableResource
):
    pass

class AccountPool(
    base.ResourcePool
):
    @property
    def wrapups(self):
        return AccountWrapupsPool(
            urljoin(self._endpoint, 'wrapups'), self._session
        )

class VoiceV1Pool(
    base.ResourcePool
):
    @property
    def campaigns(self):
        return CampaignsPool(
            urljoin(self._endpoint, 'campaigns'), self._session
        )

class VoiceV2Pool(
    base.ResourcePool
):
    @property
    def campaigns(self):
        return CampaignsV2Pool(
            urljoin(self._endpoint, 'campaigns'), self._session
        )

class V1Pool(
    base.ResourcePool
):
    @property
    def voice(self):
        return VoiceV1Pool(
            urljoin(self._endpoint, 'voice'), self._session
        )
    
    @property
    def account(self):
        return AccountPool(
            urljoin(self._endpoint, 'account'), self._session
        )

class V2Pool(
    base.ResourcePool
):
    @property
    def voice(self):
        return VoiceV2Pool(
            urljoin(self._endpoint, 'voice'), self._session
        )