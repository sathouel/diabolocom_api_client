from diabolocom_api_client.utils import urljoin
from . import base
from .campaigns import CampaignsPool, CampaignsV2Pool


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

class V2Pool(
    base.ResourcePool
):
    @property
    def voice(self):
        return VoiceV2Pool(
            urljoin(self._endpoint, 'voice'), self._session
        )