from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('172.30.53.6', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('adtran', 'adProdPartNumber', 0)).addAsn1MibSource('file:///Users//e0148840//Desktop//adtran.mib')),
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))