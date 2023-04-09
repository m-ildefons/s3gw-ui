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

from typing import AsyncGenerator

import pytest

from backend.api import S3GWClient
from backend.tests.mock_server import MotoService


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture
async def s3_server() -> AsyncGenerator[str, None]:
    async with MotoService("s3") as svc:
        yield svc.endpoint_url


@pytest.fixture
async def s3_client(s3_server: str) -> AsyncGenerator[S3GWClient, None]:
    yield S3GWClient(s3_server, "foo", "bar")
