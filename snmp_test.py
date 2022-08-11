import netsnmp
session = netsnmp.Session( DestHost='10.254.7.162', Version=2, Community='public' )
vars = netsnmp.VarList( netsnmp.Varbind('1.3.6.1.4.1.7262') )
print( session.get(vars) )
