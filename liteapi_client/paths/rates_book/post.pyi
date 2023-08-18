# coding: utf-8



from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from liteapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from liteapi_client import schemas  # noqa: F401

# body param


class SchemaForRequestBodyApplicationJson(
    schemas.AnyTypeSchema,
):


    class MetaOapg:
        required = {
            "prebookId",
            "guestInfo",
        }
        
        class properties:
            prebookId = schemas.AnyTypeSchema
            
            
            class guestInfo(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    required = {
                        "prebookId",
                        "guestLastName",
                        "guestFirstName",
                        "guestEmail",
                    }
                    
                    class properties:
                        guestFirstName = schemas.AnyTypeSchema
                        guestLastName = schemas.AnyTypeSchema
                        guestEmail = schemas.AnyTypeSchema
                        __annotations__ = {
                            "guestFirstName": guestFirstName,
                            "guestLastName": guestLastName,
                            "guestEmail": guestEmail,
                        }
            
                
                prebookId: schemas.AnyTypeSchema
                guestLastName: MetaOapg.properties.guestLastName
                guestFirstName: MetaOapg.properties.guestFirstName
                guestEmail: MetaOapg.properties.guestEmail
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["guestFirstName"]) -> MetaOapg.properties.guestFirstName: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["guestLastName"]) -> MetaOapg.properties.guestLastName: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["guestEmail"]) -> MetaOapg.properties.guestEmail: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["guestFirstName", "guestLastName", "guestEmail", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["guestFirstName"]) -> MetaOapg.properties.guestFirstName: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["guestLastName"]) -> MetaOapg.properties.guestLastName: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["guestEmail"]) -> MetaOapg.properties.guestEmail: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["guestFirstName", "guestLastName", "guestEmail", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    prebookId: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    guestLastName: typing.Union[MetaOapg.properties.guestLastName, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    guestFirstName: typing.Union[MetaOapg.properties.guestFirstName, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    guestEmail: typing.Union[MetaOapg.properties.guestEmail, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'guestInfo':
                    return super().__new__(
                        cls,
                        *_args,
                        prebookId=prebookId,
                        guestLastName=guestLastName,
                        guestFirstName=guestFirstName,
                        guestEmail=guestEmail,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class payment(
                schemas.AnyTypeSchema,
            ):
            
            
                class MetaOapg:
                    required = {
                        "holderName",
                        "method",
                    }
                    
                    class properties:
                        holderName = schemas.AnyTypeSchema
                        number = schemas.AnyTypeSchema
                        expireDate = schemas.AnyTypeSchema
                        cvc = schemas.AnyTypeSchema
                        
                        
                        class method(
                            schemas.AnyTypeSchema,
                        ):
                        
                        
                            class MetaOapg:
                                enum_value_to_name = {
                                    "CREDIT_CARD": "CREDIT_CARD",
                                    "STRIPE_TOKEN": "STRIPE_TOKEN",
                                }
                            
                            @schemas.classproperty
                            def CREDIT_CARD(cls):
                                return cls("CREDIT_CARD")
                            
                            @schemas.classproperty
                            def STRIPE_TOKEN(cls):
                                return cls("STRIPE_TOKEN")
                        
                        
                            def __new__(
                                cls,
                                *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                            ) -> 'method':
                                return super().__new__(
                                    cls,
                                    *_args,
                                    _configuration=_configuration,
                                    **kwargs,
                                )
                        token = schemas.AnyTypeSchema
                        __annotations__ = {
                            "holderName": holderName,
                            "number": number,
                            "expireDate": expireDate,
                            "cvc": cvc,
                            "method": method,
                            "token": token,
                        }
            
                
                holderName: MetaOapg.properties.holderName
                method: MetaOapg.properties.method
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["holderName"]) -> MetaOapg.properties.holderName: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["expireDate"]) -> MetaOapg.properties.expireDate: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["cvc"]) -> MetaOapg.properties.cvc: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["token"]) -> MetaOapg.properties.token: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["holderName", "number", "expireDate", "cvc", "method", "token", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["holderName"]) -> MetaOapg.properties.holderName: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["expireDate"]) -> typing.Union[MetaOapg.properties.expireDate, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["cvc"]) -> typing.Union[MetaOapg.properties.cvc, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["token"]) -> typing.Union[MetaOapg.properties.token, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["holderName", "number", "expireDate", "cvc", "method", "token", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    holderName: typing.Union[MetaOapg.properties.holderName, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    method: typing.Union[MetaOapg.properties.method, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    number: typing.Union[MetaOapg.properties.number, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    expireDate: typing.Union[MetaOapg.properties.expireDate, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    cvc: typing.Union[MetaOapg.properties.cvc, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    token: typing.Union[MetaOapg.properties.token, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'payment':
                    return super().__new__(
                        cls,
                        *_args,
                        holderName=holderName,
                        method=method,
                        number=number,
                        expireDate=expireDate,
                        cvc=cvc,
                        token=token,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "prebookId": prebookId,
                "guestInfo": guestInfo,
                "payment": payment,
            }

    
    prebookId: MetaOapg.properties.prebookId
    guestInfo: MetaOapg.properties.guestInfo
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prebookId"]) -> MetaOapg.properties.prebookId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["guestInfo"]) -> MetaOapg.properties.guestInfo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> MetaOapg.properties.payment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["prebookId", "guestInfo", "payment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prebookId"]) -> MetaOapg.properties.prebookId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["guestInfo"]) -> MetaOapg.properties.guestInfo: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> typing.Union[MetaOapg.properties.payment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["prebookId", "guestInfo", "payment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        prebookId: typing.Union[MetaOapg.properties.prebookId, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        guestInfo: typing.Union[MetaOapg.properties.guestInfo, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        payment: typing.Union[MetaOapg.properties.payment, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            prebookId=prebookId,
            guestInfo=guestInfo,
            payment=payment,
            _configuration=_configuration,
            **kwargs,
        )


request_body_any_type = api_client.RequestBody(
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
DateSchema = schemas.AnyTypeSchema
ContentTypeSchema = schemas.AnyTypeSchema
ContentLengthSchema = schemas.AnyTypeSchema
ConnectionSchema = schemas.AnyTypeSchema
XAmznRequestIdSchema = schemas.AnyTypeSchema
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
ContentEncodingSchema = schemas.AnyTypeSchema
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
XAmznRemappedContentLengthSchema = schemas.AnyTypeSchema
XAmzApigwIdSchema = schemas.AnyTypeSchema
AccessControlAllowMethodsSchema = schemas.AnyTypeSchema
AccessControlExposeHeadersSchema = schemas.AnyTypeSchema
XAmznRemappedDateSchema = schemas.AnyTypeSchema
AccessControlMaxAgeSchema = schemas.AnyTypeSchema
AccessControlAllowCredentialsSchema = schemas.AnyTypeSchema
SchemaFor200ResponseBodyApplicationJson = schemas.AnyTypeSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'Date': DateSchema,
        'Content-Type': ContentTypeSchema,
        'Content-Length': ContentLengthSchema,
        'Connection': ConnectionSchema,
        'x-amzn-RequestId': XAmznRequestIdSchema,
        'Access-Control-Allow-Origin': AccessControlAllowOriginSchema,
        'Content-Encoding': ContentEncodingSchema,
        'Access-Control-Allow-Headers': AccessControlAllowHeadersSchema,
        'x-amzn-Remapped-Content-Length': XAmznRemappedContentLengthSchema,
        'x-amz-apigw-id': XAmzApigwIdSchema,
        'Access-Control-Allow-Methods': AccessControlAllowMethodsSchema,
        'Access-Control-Expose-Headers': AccessControlExposeHeadersSchema,
        'x-amzn-Remapped-Date': XAmznRemappedDateSchema,
        'Access-Control-Max-Age': AccessControlMaxAgeSchema,
        'Access-Control-Allow-Credentials': AccessControlAllowCredentialsSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor200


_response_for_200 = api_client.LiteApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        date_parameter,
        content_type_parameter,
        content_length_parameter,
        connection_parameter,
        x_amzn_request_id_parameter,
        access_control_allow_origin_parameter,
        content_encoding_parameter,
        access_control_allow_headers_parameter,
        x_amzn_remapped_content_length_parameter,
        x_amz_apigw_id_parameter,
        access_control_allow_methods_parameter,
        access_control_expose_headers_parameter,
        x_amzn_remapped_date_parameter,
        access_control_max_age_parameter,
        access_control_allow_credentials_parameter,
    ]
)
DateSchema = schemas.AnyTypeSchema
ContentTypeSchema = schemas.AnyTypeSchema
ContentLengthSchema = schemas.AnyTypeSchema
ConnectionSchema = schemas.AnyTypeSchema
XAmznRequestIdSchema = schemas.AnyTypeSchema
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
ContentEncodingSchema = schemas.AnyTypeSchema
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
XAmznRemappedContentLengthSchema = schemas.AnyTypeSchema
XAmzApigwIdSchema = schemas.AnyTypeSchema
AccessControlAllowMethodsSchema = schemas.AnyTypeSchema
AccessControlExposeHeadersSchema = schemas.AnyTypeSchema
XAmznRemappedDateSchema = schemas.AnyTypeSchema
AccessControlMaxAgeSchema = schemas.AnyTypeSchema
AccessControlAllowCredentialsSchema = schemas.AnyTypeSchema
SchemaFor400ResponseBodyApplicationJson = schemas.AnyTypeSchema
ResponseHeadersFor400 = typing_extensions.TypedDict(
    'ResponseHeadersFor400',
    {
        'Date': DateSchema,
        'Content-Type': ContentTypeSchema,
        'Content-Length': ContentLengthSchema,
        'Connection': ConnectionSchema,
        'x-amzn-RequestId': XAmznRequestIdSchema,
        'Access-Control-Allow-Origin': AccessControlAllowOriginSchema,
        'Content-Encoding': ContentEncodingSchema,
        'Access-Control-Allow-Headers': AccessControlAllowHeadersSchema,
        'x-amzn-Remapped-Content-Length': XAmznRemappedContentLengthSchema,
        'x-amz-apigw-id': XAmzApigwIdSchema,
        'Access-Control-Allow-Methods': AccessControlAllowMethodsSchema,
        'Access-Control-Expose-Headers': AccessControlExposeHeadersSchema,
        'x-amzn-Remapped-Date': XAmznRemappedDateSchema,
        'Access-Control-Max-Age': AccessControlMaxAgeSchema,
        'Access-Control-Allow-Credentials': AccessControlAllowCredentialsSchema,
    }
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor400


_response_for_400 = api_client.LiteApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
    headers=[
        date_parameter,
        content_type_parameter,
        content_length_parameter,
        connection_parameter,
        x_amzn_request_id_parameter,
        access_control_allow_origin_parameter,
        content_encoding_parameter,
        access_control_allow_headers_parameter,
        x_amzn_remapped_content_length_parameter,
        x_amz_apigw_id_parameter,
        access_control_allow_methods_parameter,
        access_control_expose_headers_parameter,
        x_amzn_remapped_date_parameter,
        access_control_max_age_parameter,
        access_control_allow_credentials_parameter,
    ]
)
DateSchema = schemas.AnyTypeSchema
ContentTypeSchema = schemas.AnyTypeSchema
ContentLengthSchema = schemas.AnyTypeSchema
ConnectionSchema = schemas.AnyTypeSchema
XAmznRequestIdSchema = schemas.AnyTypeSchema
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
ContentEncodingSchema = schemas.AnyTypeSchema
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
XAmznRemappedContentLengthSchema = schemas.AnyTypeSchema
XAmzApigwIdSchema = schemas.AnyTypeSchema
AccessControlAllowMethodsSchema = schemas.AnyTypeSchema
AccessControlExposeHeadersSchema = schemas.AnyTypeSchema
XAmznRemappedDateSchema = schemas.AnyTypeSchema
AccessControlMaxAgeSchema = schemas.AnyTypeSchema
AccessControlAllowCredentialsSchema = schemas.AnyTypeSchema
SchemaFor401ResponseBodyApplicationJson = schemas.AnyTypeSchema
ResponseHeadersFor401 = typing_extensions.TypedDict(
    'ResponseHeadersFor401',
    {
        'Date': DateSchema,
        'Content-Type': ContentTypeSchema,
        'Content-Length': ContentLengthSchema,
        'Connection': ConnectionSchema,
        'x-amzn-RequestId': XAmznRequestIdSchema,
        'Access-Control-Allow-Origin': AccessControlAllowOriginSchema,
        'Content-Encoding': ContentEncodingSchema,
        'Access-Control-Allow-Headers': AccessControlAllowHeadersSchema,
        'x-amzn-Remapped-Content-Length': XAmznRemappedContentLengthSchema,
        'x-amz-apigw-id': XAmzApigwIdSchema,
        'Access-Control-Allow-Methods': AccessControlAllowMethodsSchema,
        'Access-Control-Expose-Headers': AccessControlExposeHeadersSchema,
        'x-amzn-Remapped-Date': XAmznRemappedDateSchema,
        'Access-Control-Max-Age': AccessControlMaxAgeSchema,
        'Access-Control-Allow-Credentials': AccessControlAllowCredentialsSchema,
    }
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor401


_response_for_401 = api_client.LiteApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
    headers=[
        date_parameter,
        content_type_parameter,
        content_length_parameter,
        connection_parameter,
        x_amzn_request_id_parameter,
        access_control_allow_origin_parameter,
        content_encoding_parameter,
        access_control_allow_headers_parameter,
        x_amzn_remapped_content_length_parameter,
        x_amz_apigw_id_parameter,
        access_control_allow_methods_parameter,
        access_control_expose_headers_parameter,
        x_amzn_remapped_date_parameter,
        access_control_max_age_parameter,
        access_control_allow_credentials_parameter,
    ]
)
_all_accept_content_types = (
    'application/json; charset=utf-8',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _book_oapg(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _book_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _book_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _book_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _book_oapg(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        hotel rate book
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_any_type.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
            book=True
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class RatesBookPost(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def book_call(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def book_call(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def book_call(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def book_call(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def book_call(
        self,
        content_type: str = 'application/json; charset=utf-8',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._book_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

    def book(
            self,
            prebookId: str,
            guestFirstName: str,
            guestLastName: str,
            guestEmail: str,
            holderName: str,
            paymentMethod: str,
            cardNumber: str = None,
            expireMonth: str = None,
            expireYear: str = None,
            cvc: str = None,
            token: str = None,
        ):
        try:
            guest_info = SchemaForRequestBodyApplicationJson.MetaOapg.properties.guestInfo(
                guestFirstName=guestFirstName,
                guestLastName=guestLastName,
                guestEmail=guestEmail
            )

            if paymentMethod == "CREDIT_CARD":
                payment = SchemaForRequestBodyApplicationJson.MetaOapg.properties.payment(
                    holderName=holderName,
                    number=cardNumber,
                    expireDate=expireMonth+"/"+expireYear,
                    cvc=cvc,
                    method=SchemaForRequestBodyApplicationJson.MetaOapg.properties.payment.MetaOapg.properties.method.CREDIT_CARD
                    
                )
            elif paymentMethod == "STRIPE_TOKEN":
                payment = SchemaForRequestBodyApplicationJson.MetaOapg.properties.payment(
                    holderName=holderName,
                    token=token,
                    method=SchemaForRequestBodyApplicationJson.MetaOapg.properties.payment.MetaOapg.properties.method.STRIPE_TOKEN
                )
            
            body = SchemaForRequestBodyApplicationJson(
                prebookId=prebookId,
                guestInfo=guest_info,
                payment=payment
                )
            
            api_response = self.book_call(
                body=body
            )
            return api_response.body
        except exceptions.ApiException as e:
            return ("Exception when calling BookApi->book: %s\n" % e)

class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._book_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


