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

# Query params
CountryCodeSchema = schemas.AnyTypeSchema
CityNameSchema = schemas.AnyTypeSchema
OffsetSchema = schemas.AnyTypeSchema
LimitSchema = schemas.AnyTypeSchema
LongitudeSchema = schemas.AnyTypeSchema
LatitudeSchema = schemas.AnyTypeSchema
DistanceSchema = schemas.AnyTypeSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'countryCode': typing.Union[CountryCodeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'cityName': typing.Union[CityNameSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'offset': typing.Union[OffsetSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'limit': typing.Union[LimitSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'longitude': typing.Union[LongitudeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'latitude': typing.Union[LatitudeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'distance': typing.Union[DistanceSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_country_code = api_client.QueryParameter(
    name="countryCode",
    style=api_client.ParameterStyle.FORM,
    schema=CountryCodeSchema,
    required=True,
    explode=True,
)
request_query_city_name = api_client.QueryParameter(
    name="cityName",
    style=api_client.ParameterStyle.FORM,
    schema=CityNameSchema,
    required=True,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_longitude = api_client.QueryParameter(
    name="longitude",
    style=api_client.ParameterStyle.FORM,
    schema=LongitudeSchema,
    explode=True,
)
request_query_latitude = api_client.QueryParameter(
    name="latitude",
    style=api_client.ParameterStyle.FORM,
    schema=LatitudeSchema,
    explode=True,
)
request_query_distance = api_client.QueryParameter(
    name="distance",
    style=api_client.ParameterStyle.FORM,
    schema=DistanceSchema,
    explode=True,
)
DateSchema = schemas.AnyTypeSchema
ContentTypeSchema = schemas.AnyTypeSchema
ContentLengthSchema = schemas.AnyTypeSchema
ConnectionSchema = schemas.AnyTypeSchema
XAmznRequestIdSchema = schemas.AnyTypeSchema
AccessControlAllowOriginSchema = schemas.AnyTypeSchema
ContentEncodingSchema = schemas.AnyTypeSchema
AccessControlAllowHeadersSchema = schemas.AnyTypeSchema
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


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
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


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
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


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json': api_client.MediaType(
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
        x_amz_apigw_id_parameter,
        access_control_allow_methods_parameter,
        access_control_expose_headers_parameter,
        x_amzn_remapped_date_parameter,
        access_control_max_age_parameter,
        access_control_allow_credentials_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_hotels_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_hotels_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_hotels_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_hotels_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Hotel list
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_country_code,
            request_query_city_name,
            request_query_offset,
            request_query_limit,
            request_query_longitude,
            request_query_latitude,
            request_query_distance,
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


class DataHotelsGet(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_hotels(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_hotels(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_hotels(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_hotels(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_hotels_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


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
        return self._get_hotels_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


