#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.16.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeploymentLB(Model):
    """
    Deployment operation parameters.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar uri: URI referencing the template. Default value:
     "https://azuresdkci.blob.core.windows.net/templatehost/CreateLB/azuredeploy.json"
     .
    :vartype uri: str
    :param content_version: If included it must match the ContentVersion in
     the template.
    :type content_version: str
    :ivar _artifacts_location: Container URI of of the template. Default
     value: "https://azuresdkci.blob.core.windows.net/templatehost/CreateLB" .
    :vartype _artifacts_location: str
    :param backend_pool_name: Name of load balancer backend pool.
    :type backend_pool_name: str
    :param dns_name_for_public_ip: Globally unique DNS Name for the Public IP
     used to access the Virtual Machine.  Requires a new public IP to be
     created by setting Public IP Address Type to New.
    :type dns_name_for_public_ip: str
    :param dns_name_type: Associate VMs with a public IP address to a DNS
     name. Possible values include: 'none', 'new'. Default value: "none" .
    :type dns_name_type: str
    :param location: Location for load balancer resource.
    :type location: str
    :param name: Name for load balancer.
    :type name: str
    :param nat_backend_port: Port number for NAT backend. Default value: "22"
     .
    :type nat_backend_port: str
    :param nat_end_port: End of NAT port range. Default value: "50099" .
    :type nat_end_port: str
    :param nat_pool_name: Name of load balancer NAT (network address
     translation) pool.
    :type nat_pool_name: str
    :param nat_start_port: Start of NAT port range. Default value: "50000" .
    :type nat_start_port: str
    :param private_ip_address_allocation: Private IP address allocation
     method. Possible values include: 'Dynamic', 'Static'. Default value:
     "Dynamic" .
    :type private_ip_address_allocation: str
    :param public_ip_address_allocation: Public IP address allocation method.
     Possible values include: 'Dynamic', 'Static'. Default value: "Dynamic" .
    :type public_ip_address_allocation: str
    :param public_ip_address_name: Name of public IP address to use.
    :type public_ip_address_name: str
    :param public_ip_address_type: Type of Public IP Address to associate
     with the laod balancer. Possible values include: 'none', 'new',
     'existing'. Default value: "new" .
    :type public_ip_address_type: str
    :param subnet_name: If Public IP address is turned off, this is the
     subnet to associate with the load balancer.
    :type subnet_name: str
    :param virtual_network_name: If Public IP address is turned off, this is
     the VNET to associate with the load balancer .
    :type virtual_network_name: str
    :ivar mode: Gets or sets the deployment mode. Default value:
     "Incremental" .
    :vartype mode: str
    """ 

    _validation = {
        'uri': {'required': True, 'constant': True},
        '_artifacts_location': {'required': True, 'constant': True},
        'name': {'required': True},
        'mode': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'uri': {'key': 'properties.templateLink.uri', 'type': 'str'},
        'content_version': {'key': 'properties.templateLink.contentVersion', 'type': 'str'},
        '_artifacts_location': {'key': 'properties.parameters._artifactsLocation.value', 'type': 'str'},
        'backend_pool_name': {'key': 'properties.parameters.backendPoolName.value', 'type': 'str'},
        'dns_name_for_public_ip': {'key': 'properties.parameters.dnsNameForPublicIP.value', 'type': 'str'},
        'dns_name_type': {'key': 'properties.parameters.dnsNameType.value', 'type': 'str'},
        'location': {'key': 'properties.parameters.location.value', 'type': 'str'},
        'name': {'key': 'properties.parameters.name.value', 'type': 'str'},
        'nat_backend_port': {'key': 'properties.parameters.natBackendPort.value', 'type': 'str'},
        'nat_end_port': {'key': 'properties.parameters.natEndPort.value', 'type': 'str'},
        'nat_pool_name': {'key': 'properties.parameters.natPoolName.value', 'type': 'str'},
        'nat_start_port': {'key': 'properties.parameters.natStartPort.value', 'type': 'str'},
        'private_ip_address_allocation': {'key': 'properties.parameters.privateIpAddressAllocation.value', 'type': 'str'},
        'public_ip_address_allocation': {'key': 'properties.parameters.publicIpAddressAllocation.value', 'type': 'str'},
        'public_ip_address_name': {'key': 'properties.parameters.publicIpAddressName.value', 'type': 'str'},
        'public_ip_address_type': {'key': 'properties.parameters.publicIpAddressType.value', 'type': 'str'},
        'subnet_name': {'key': 'properties.parameters.subnetName.value', 'type': 'str'},
        'virtual_network_name': {'key': 'properties.parameters.virtualNetworkName.value', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
    }

    uri = "https://azuresdkci.blob.core.windows.net/templatehost/CreateLB/azuredeploy.json"

    _artifacts_location = "https://azuresdkci.blob.core.windows.net/templatehost/CreateLB"

    mode = "Incremental"

    def __init__(self, name, content_version=None, backend_pool_name=None, dns_name_for_public_ip=None, dns_name_type="none", location=None, nat_backend_port="22", nat_end_port="50099", nat_pool_name=None, nat_start_port="50000", private_ip_address_allocation="Dynamic", public_ip_address_allocation="Dynamic", public_ip_address_name=None, public_ip_address_type="new", subnet_name=None, virtual_network_name=None):
        self.content_version = content_version
        self.backend_pool_name = backend_pool_name
        self.dns_name_for_public_ip = dns_name_for_public_ip
        self.dns_name_type = dns_name_type
        self.location = location
        self.name = name
        self.nat_backend_port = nat_backend_port
        self.nat_end_port = nat_end_port
        self.nat_pool_name = nat_pool_name
        self.nat_start_port = nat_start_port
        self.private_ip_address_allocation = private_ip_address_allocation
        self.public_ip_address_allocation = public_ip_address_allocation
        self.public_ip_address_name = public_ip_address_name
        self.public_ip_address_type = public_ip_address_type
        self.subnet_name = subnet_name
        self.virtual_network_name = virtual_network_name
