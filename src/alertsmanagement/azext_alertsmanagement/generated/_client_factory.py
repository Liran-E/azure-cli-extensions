# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_alertsmanagement_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_alertsmanagement.vendored_sdks.alertsmanagement import AlertsManagementClient
    return get_mgmt_service_client(cli_ctx,
                                   AlertsManagementClient)


def cf_alert_processing_rule(cli_ctx, *_):
    return cf_alertsmanagement_cl(cli_ctx).alert_processing_rules


def cf_alert(cli_ctx, *_):
    return cf_alertsmanagement_cl(cli_ctx).alerts


def cf_smart_group(cli_ctx, *_):
    return cf_alertsmanagement_cl(cli_ctx).smart_groups
