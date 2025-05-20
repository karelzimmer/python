import  java


node_ids = AdminConfig.list( 'Node' ).split("\n")

cellname = AdminControl.getCell()
scope = '(cell):%s' % (cellname)
try:
    AdminTask.modifySSLConfig('[-alias CellDefaultSSLSettings -scopeName %s  -sslProtocol TLSv1.2]' % (scope))
    AdminTask.modifySSLConfig('[-alias XDADefaultSSLSettings  -scopeName %s  -sslProtocol TLSv1.2]' % (scope))
except:
    print "CellDefaultSSLSettings are not changed for scope" + scope

scope = ''

for node_id in node_ids:
        nodename = AdminConfig.showAttribute(node_id, 'name')
        #nodename = getNodeName(node_id)
        serverEntries = AdminConfig.list( 'ServerEntry', node_id ).split("\n")
        for serverEntry in serverEntries:
                serverName = AdminConfig.showAttribute( serverEntry, "serverName" )
                serverType = AdminConfig.showAttribute( serverEntry, "serverType" )
                if serverType == "APPLICATION_SERVER":
                        print serverName + " " + serverType + " " + nodename
                        scope = '(cell):%s:(node):%s' % (cellname, nodename)
                        print "scope= " + scope
                        AdminTask.modifySSLConfig('[-alias NodeDefaultSSLSettings  -scopeName %s  -sslProtocol TLSv1.2]' % (scope))
                        AdminConfig.save() 
