# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List
from Tea.core import TeaCore

from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> ocr_api20210707Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:

        client = Sample.create_client('204120628', 'TLMmvHVGt5fMp6G5sgAA8psAiTx7AhTG')
        # 需要安装额外的依赖库，直接点击下载完整工程即可看到所有依赖。
        body_syream = StreamClient.read_from_file_path('resource/DYEA.png')
        recognize_general_request = ocr_api_20210707_models.RecognizeGeneralRequest(
            body=body_syream
        )
        runtime = util_models.RuntimeOptions()
        resp = client.recognize_general_with_options(recognize_general_request, runtime)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('ACCESS_KEY_ID', 'ACCESS_KEY_SECRET')
        # 需要安装额外的依赖库，直接点击下载完整工程即可看到所有依赖。
        body_syream = StreamClient.read_from_file_path('<your-file-path>')
        recognize_general_request = ocr_api_20210707_models.RecognizeGeneralRequest(
            body=body_syream
        )
        runtime = util_models.RuntimeOptions()
        resp = await client.recognize_general_with_options_async(recognize_general_request, runtime)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
