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

from . import path

# Query params
HotelIdsSchema = schemas.AnyTypeSchema
CheckinSchema = schemas.AnyTypeSchema
CheckoutSchema = schemas.AnyTypeSchema
CurrencySchema = schemas.AnyTypeSchema
GuestNationalitySchema = schemas.AnyTypeSchema
AdultsSchema = schemas.AnyTypeSchema
ChildrenSchema = schemas.AnyTypeSchema
GuestIdSchema = schemas.AnyTypeSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'hotelIds': typing.Union[HotelIdsSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'checkin': typing.Union[CheckinSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'checkout': typing.Union[CheckoutSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'currency': typing.Union[CurrencySchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'guestNationality': typing.Union[GuestNationalitySchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'adults': typing.Union[AdultsSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'children': typing.Union[ChildrenSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'guestId': typing.Union[GuestIdSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_hotel_ids = api_client.QueryParameter(
    name="hotelIds",
    style=api_client.ParameterStyle.FORM,
    schema=HotelIdsSchema,
    required=True,
    explode=True,
)
request_query_checkin = api_client.QueryParameter(
    name="checkin",
    style=api_client.ParameterStyle.FORM,
    schema=CheckinSchema,
    required=True,
    explode=True,
)
request_query_checkout = api_client.QueryParameter(
    name="checkout",
    style=api_client.ParameterStyle.FORM,
    schema=CheckoutSchema,
    required=True,
    explode=True,
)
request_query_currency = api_client.QueryParameter(
    name="currency",
    style=api_client.ParameterStyle.FORM,
    schema=CurrencySchema,
    required=True,
    explode=True,
)
request_query_guest_nationality = api_client.QueryParameter(
    name="guestNationality",
    style=api_client.ParameterStyle.FORM,
    schema=GuestNationalitySchema,
    required=True,
    explode=True,
)
request_query_adults = api_client.QueryParameter(
    name="adults",
    style=api_client.ParameterStyle.FORM,
    schema=AdultsSchema,
    required=True,
    explode=True,
)
request_query_children = api_client.QueryParameter(
    name="children",
    style=api_client.ParameterStyle.FORM,
    schema=ChildrenSchema,
    explode=True,
)
request_query_guest_id = api_client.QueryParameter(
    name="guestId",
    style=api_client.ParameterStyle.FORM,
    schema=GuestIdSchema,
    explode=True,
)
_auth = [
    'apikeyAuth',
]
DateSchema = schemas.AnyTypeSchema
date_parameter = api_client.HeaderParameter(
    name="Date",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DateSchema,
)
ContentTypeSchema = schemas.AnyTypeSchema
content_type_parameter = api_client.HeaderParameter(
    name="Content-Type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentTypeSchema,
)
ContentLengthSchema = schemas.AnyTypeSchema
content_length_parameter = api_client.HeaderParameter(
    name="Content-Length",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentLengthSchema,
)
ConnectionSchema = schemas.AnyTypeSchema
connection_parameter = api_client.HeaderParameter(
    name="Connection",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ConnectionSchema,
)
XAmznRequestIdSchema = schemas.AnyTypeSchema
x_amzn_request_id_parameter = api_client.HeaderParameter(
    name="x-amzn-RequestId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAmznRequestIdSchema,
)
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
access_control_allow_origin_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Origin",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowOriginSchema,
)
ContentEncodingSchema = schemas.AnyTypeSchema
content_encoding_parameter = api_client.HeaderParameter(
    name="Content-Encoding",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentEncodingSchema,
)
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
access_control_allow_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowHeadersSchema,
)
XAmznRemappedContentLengthSchema = schemas.AnyTypeSchema
x_amzn_remapped_content_length_parameter = api_client.HeaderParameter(
    name="x-amzn-Remapped-Content-Length",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAmznRemappedContentLengthSchema,
)
XAmzApigwIdSchema = schemas.AnyTypeSchema
x_amz_apigw_id_parameter = api_client.HeaderParameter(
    name="x-amz-apigw-id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAmzApigwIdSchema,
)
AccessControlAllowMethodsSchema = schemas.AnyTypeSchema
access_control_allow_methods_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Methods",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowMethodsSchema,
)
AccessControlExposeHeadersSchema = schemas.AnyTypeSchema
access_control_expose_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Expose-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlExposeHeadersSchema,
)
XAmznRemappedDateSchema = schemas.AnyTypeSchema
x_amzn_remapped_date_parameter = api_client.HeaderParameter(
    name="x-amzn-Remapped-Date",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XAmznRemappedDateSchema,
)
AccessControlMaxAgeSchema = schemas.AnyTypeSchema
access_control_max_age_parameter = api_client.HeaderParameter(
    name="Access-Control-Max-Age",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlMaxAgeSchema,
)
AccessControlAllowCredentialsSchema = schemas.AnyTypeSchema
access_control_allow_credentials_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Credentials",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowCredentialsSchema,
)
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
AccessControlAllowCredentialsSchema = schemas.AnyTypeSchema
access_control_allow_credentials_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Credentials",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowCredentialsSchema,
)
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
access_control_allow_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowHeadersSchema,
)
AccessControlAllowMethodsSchema = schemas.AnyTypeSchema
access_control_allow_methods_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Methods",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowMethodsSchema,
)
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
access_control_allow_origin_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Origin",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowOriginSchema,
)
AccessControlExposeHeadersSchema = schemas.AnyTypeSchema
access_control_expose_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Expose-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlExposeHeadersSchema,
)
AccessControlMaxAgeSchema = schemas.AnyTypeSchema
access_control_max_age_parameter = api_client.HeaderParameter(
    name="Access-Control-Max-Age",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlMaxAgeSchema,
)
ContentTypeSchema = schemas.AnyTypeSchema
content_type_parameter = api_client.HeaderParameter(
    name="Content-Type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentTypeSchema,
)
DateSchema = schemas.AnyTypeSchema
date_parameter = api_client.HeaderParameter(
    name="Date",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DateSchema,
)
ContentLengthSchema = schemas.AnyTypeSchema
content_length_parameter = api_client.HeaderParameter(
    name="Content-Length",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentLengthSchema,
)
SchemaFor204ResponseBodyApplicationJson = schemas.AnyTypeSchema
ResponseHeadersFor204 = typing_extensions.TypedDict(
    'ResponseHeadersFor204',
    {
        'Access-Control-Allow-Credentials': AccessControlAllowCredentialsSchema,
        'Access-Control-Allow-Headers': AccessControlAllowHeadersSchema,
        'Access-Control-Allow-Methods': AccessControlAllowMethodsSchema,
        'Access-Control-Allow-Origin': AccessControlAllowOriginSchema,
        'Access-Control-Expose-Headers': AccessControlExposeHeadersSchema,
        'Access-Control-Max-Age': AccessControlMaxAgeSchema,
        'Content-Type': ContentTypeSchema,
        'Date': DateSchema,
        'Content-Length': ContentLengthSchema,
    }
)


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor204ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor204


_response_for_204 = api_client.LiteApiResponse(
    response_cls=ApiResponseFor204,
    content={
        'application/json; charset=utf-8': api_client.MediaType(
            schema=SchemaFor204ResponseBodyApplicationJson),
    },
    headers=[
        access_control_allow_credentials_parameter,
        access_control_allow_headers_parameter,
        access_control_allow_methods_parameter,
        access_control_allow_origin_parameter,
        access_control_expose_headers_parameter,
        access_control_max_age_parameter,
        content_type_parameter,
        date_parameter,
        content_length_parameter,
    ]
)
AccessControlAllowCredentialsSchema = schemas.AnyTypeSchema
access_control_allow_credentials_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Credentials",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowCredentialsSchema,
)
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
access_control_allow_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowHeadersSchema,
)
AccessControlAllowMethodsSchema = schemas.AnyTypeSchema
access_control_allow_methods_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Methods",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowMethodsSchema,
)
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
access_control_allow_origin_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Origin",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowOriginSchema,
)
AccessControlExposeHeadersSchema = schemas.AnyTypeSchema
access_control_expose_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Expose-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlExposeHeadersSchema,
)
AccessControlMaxAgeSchema = schemas.AnyTypeSchema
access_control_max_age_parameter = api_client.HeaderParameter(
    name="Access-Control-Max-Age",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlMaxAgeSchema,
)
ContentTypeSchema = schemas.AnyTypeSchema
content_type_parameter = api_client.HeaderParameter(
    name="Content-Type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentTypeSchema,
)
DateSchema = schemas.AnyTypeSchema
date_parameter = api_client.HeaderParameter(
    name="Date",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DateSchema,
)
ContentLengthSchema = schemas.AnyTypeSchema
content_length_parameter = api_client.HeaderParameter(
    name="Content-Length",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentLengthSchema,
)
SchemaFor400ResponseBodyApplicationJson = schemas.AnyTypeSchema
ResponseHeadersFor400 = typing_extensions.TypedDict(
    'ResponseHeadersFor400',
    {
        'Access-Control-Allow-Credentials': AccessControlAllowCredentialsSchema,
        'Access-Control-Allow-Headers': AccessControlAllowHeadersSchema,
        'Access-Control-Allow-Methods': AccessControlAllowMethodsSchema,
        'Access-Control-Allow-Origin': AccessControlAllowOriginSchema,
        'Access-Control-Expose-Headers': AccessControlExposeHeadersSchema,
        'Access-Control-Max-Age': AccessControlMaxAgeSchema,
        'Content-Type': ContentTypeSchema,
        'Date': DateSchema,
        'Content-Length': ContentLengthSchema,
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
        access_control_allow_credentials_parameter,
        access_control_allow_headers_parameter,
        access_control_allow_methods_parameter,
        access_control_allow_origin_parameter,
        access_control_expose_headers_parameter,
        access_control_max_age_parameter,
        content_type_parameter,
        date_parameter,
        content_length_parameter,
    ]
)
AccessControlAllowCredentialsSchema = schemas.AnyTypeSchema
access_control_allow_credentials_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Credentials",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowCredentialsSchema,
)
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
access_control_allow_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowHeadersSchema,
)
AccessControlAllowMethodsSchema = schemas.AnyTypeSchema
access_control_allow_methods_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Methods",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowMethodsSchema,
)
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
access_control_allow_origin_parameter = api_client.HeaderParameter(
    name="Access-Control-Allow-Origin",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlAllowOriginSchema,
)
AccessControlExposeHeadersSchema = schemas.AnyTypeSchema
access_control_expose_headers_parameter = api_client.HeaderParameter(
    name="Access-Control-Expose-Headers",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlExposeHeadersSchema,
)
AccessControlMaxAgeSchema = schemas.AnyTypeSchema
access_control_max_age_parameter = api_client.HeaderParameter(
    name="Access-Control-Max-Age",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AccessControlMaxAgeSchema,
)
ContentTypeSchema = schemas.AnyTypeSchema
content_type_parameter = api_client.HeaderParameter(
    name="Content-Type",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentTypeSchema,
)
DateSchema = schemas.AnyTypeSchema
date_parameter = api_client.HeaderParameter(
    name="Date",
    style=api_client.ParameterStyle.SIMPLE,
    schema=DateSchema,
)
ContentLengthSchema = schemas.AnyTypeSchema
content_length_parameter = api_client.HeaderParameter(
    name="Content-Length",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentLengthSchema,
)
SchemaFor401ResponseBodyApplicationJson = schemas.AnyTypeSchema
ResponseHeadersFor401 = typing_extensions.TypedDict(
    'ResponseHeadersFor401',
    {
        'Access-Control-Allow-Credentials': AccessControlAllowCredentialsSchema,
        'Access-Control-Allow-Headers': AccessControlAllowHeadersSchema,
        'Access-Control-Allow-Methods': AccessControlAllowMethodsSchema,
        'Access-Control-Allow-Origin': AccessControlAllowOriginSchema,
        'Access-Control-Expose-Headers': AccessControlExposeHeadersSchema,
        'Access-Control-Max-Age': AccessControlMaxAgeSchema,
        'Content-Type': ContentTypeSchema,
        'Date': DateSchema,
        'Content-Length': ContentLengthSchema,
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
        access_control_allow_credentials_parameter,
        access_control_allow_headers_parameter,
        access_control_allow_methods_parameter,
        access_control_allow_origin_parameter,
        access_control_expose_headers_parameter,
        access_control_max_age_parameter,
        content_type_parameter,
        date_parameter,
        content_length_parameter,
    ]
)
_status_code_to_response = {
    '200': _response_for_200,
    '204': _response_for_204,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json; charset=utf-8',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_minimum_rates_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor204,
    ]: ...

    @typing.overload
    def _get_minimum_rates_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_minimum_rates_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_minimum_rates_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        hotel minimum rates availability
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_hotel_ids,
            request_query_checkin,
            request_query_checkout,
            request_query_currency,
            request_query_guest_nationality,
            request_query_adults,
            request_query_children,
            request_query_guest_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
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


class HotelsGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_minimum_rates_call(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor204,
    ]: ...

    @typing.overload
    def get_minimum_rates_call(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_minimum_rates_call(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_minimum_rates_call(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_minimum_rates_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )

    def get_minimum_rates(
            self,
            hotelIds: str,
            checkin: str,
            checkout: str,
            currency: str,
            guestNationality: str,
            adults: str,
            children:str,
            guestId:str
        ):
        try:
            query_params = {
                    hotelIds: hotelIds,
                    checkin: checkin,
                    checkout: checkout,
                    currency: currency,
                    guestNationality: guestNationality,
                    adults: adults,
                    children:children,
                    guestId:guestId
                }
            api_response = self.get_minimum_rates_call(
                query_params=query_params
            )
            return api_response.body
        except exceptions.ApiException as e:
            return ("Exception when calling SearchApi->get_minimum_rates: %s\n" % e)
        


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor204,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_minimum_rates_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


