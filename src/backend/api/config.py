# Copyright 2023 SUSE LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fastapi import Request
from fastapi.routing import APIRouter
from pydantic import BaseModel

from backend.config import Config


class ConfigResponse(BaseModel):
    Endpoint: str
    InstanceId: str
    Delimiter: str
    ApiPath: str


router = APIRouter(prefix="/config", tags=["config"])


@router.get(
    "/",
    response_model=ConfigResponse,
)
async def get_config(req: Request) -> ConfigResponse:
    config: Config = req.app.state.config
    return ConfigResponse.parse_obj(config.to_dict())
