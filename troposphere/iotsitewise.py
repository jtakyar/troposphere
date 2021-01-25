# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 25.0.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags


class User(AWSProperty):
    props = {
        'id': (basestring, False),
    }


class AccessPolicyIdentity(AWSProperty):
    props = {
        'User': (User, False),
    }


class Portal(AWSProperty):
    props = {
        'id': (basestring, False),
    }


class Project(AWSProperty):
    props = {
        'id': (basestring, False),
    }


class AccessPolicyResource(AWSProperty):
    props = {
        'Portal': (Portal, False),
        'Project': (Project, False),
    }


class AccessPolicy(AWSObject):
    resource_type = "AWS::IoTSiteWise::AccessPolicy"

    props = {
        'AccessPolicyIdentity': (AccessPolicyIdentity, True),
        'AccessPolicyPermission': (basestring, True),
        'AccessPolicyResource': (AccessPolicyResource, True),
    }


class AssetHierarchy(AWSProperty):
    props = {
        'ChildAssetId': (basestring, True),
        'LogicalId': (basestring, True),
    }


class AssetProperty(AWSProperty):
    props = {
        'Alias': (basestring, False),
        'LogicalId': (basestring, True),
        'NotificationState': (basestring, False),
    }


class Asset(AWSObject):
    resource_type = "AWS::IoTSiteWise::Asset"

    props = {
        'AssetHierarchies': ([AssetHierarchy], False),
        'AssetModelId': (basestring, True),
        'AssetName': (basestring, True),
        'AssetProperties': ([AssetProperty], False),
        'Tags': (Tags, False),
    }


class AssetModelHierarchy(AWSProperty):
    props = {
        'ChildAssetModelId': (basestring, True),
        'LogicalId': (basestring, True),
        'Name': (basestring, True),
    }


class Attribute(AWSProperty):
    props = {
        'DefaultValue': (basestring, False),
    }


class VariableValue(AWSProperty):
    props = {
        'HierarchyLogicalId': (basestring, False),
        'PropertyLogicalId': (basestring, True),
    }


class ExpressionVariable(AWSProperty):
    props = {
        'Name': (basestring, True),
        'Value': (VariableValue, True),
    }


class TumblingWindow(AWSProperty):
    props = {
        'Interval': (basestring, True),
    }


class MetricWindow(AWSProperty):
    props = {
        'Tumbling': (TumblingWindow, False),
    }


class Metric(AWSProperty):
    props = {
        'Expression': (basestring, True),
        'Variables': ([ExpressionVariable], True),
        'Window': (MetricWindow, True),
    }


class Transform(AWSProperty):
    props = {
        'Expression': (basestring, True),
        'Variables': ([ExpressionVariable], True),
    }


class PropertyType(AWSProperty):
    props = {
        'Attribute': (Attribute, False),
        'Metric': (Metric, False),
        'Transform': (Transform, False),
        'TypeName': (basestring, True),
    }


class AssetModelProperty(AWSProperty):
    props = {
        'DataType': (basestring, True),
        'LogicalId': (basestring, True),
        'Name': (basestring, True),
        'Type': (PropertyType, True),
        'Unit': (basestring, False),
    }


class AssetModel(AWSObject):
    resource_type = "AWS::IoTSiteWise::AssetModel"

    props = {
        'AssetModelDescription': (basestring, False),
        'AssetModelHierarchies': ([AssetModelHierarchy], False),
        'AssetModelName': (basestring, True),
        'AssetModelProperties': ([AssetModelProperty], False),
        'Tags': (Tags, False),
    }


class Dashboard(AWSObject):
    resource_type = "AWS::IoTSiteWise::Dashboard"

    props = {
        'DashboardDefinition': (basestring, True),
        'DashboardDescription': (basestring, True),
        'DashboardName': (basestring, True),
        'ProjectId': (basestring, False),
        'Tags': (Tags, False),
    }


class GatewayCapabilitySummary(AWSProperty):
    props = {
        'CapabilityConfiguration': (basestring, False),
        'CapabilityNamespace': (basestring, True),
    }


class Greengrass(AWSProperty):
    props = {
        'GroupArn': (basestring, True),
    }


class GatewayPlatform(AWSProperty):
    props = {
        'Greengrass': (Greengrass, True),
    }


class Gateway(AWSObject):
    resource_type = "AWS::IoTSiteWise::Gateway"

    props = {
        'GatewayCapabilitySummaries': ([GatewayCapabilitySummary], False),
        'GatewayName': (basestring, True),
        'GatewayPlatform': (GatewayPlatform, True),
        'Tags': (Tags, False),
    }
