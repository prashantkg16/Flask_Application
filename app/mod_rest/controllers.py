# Import flask dependencies
from flask import Blueprint, Flask, jsonify, request
from collections import OrderedDict
from app import mysqldb


# Import module models
from app.mod_rest.models import Server, Servergroup, Monitorgroup, PluginRunScript, PluginMariaDB, Pluginmysql, PluginProc, PluginFileSpace, PluginLog, PluginUrl

# Define the blueprint
mod_rest = Blueprint('rest', __name__, url_prefix='/rest')

@mod_rest.route('/api/v1/<api_method>/<server_name>/<data_format>', methods=['GET', 'POST'])
def api(api_method,server_name,data_format):
	qsDict = OrderedDict()
	logList = list()
	logDict = OrderedDict()
	qsDict['serverName'] =  server_name
	qsDict['flag'] = "DA"
	qsDict.move_to_end('flag', last=False)
	try:
		if api_method == "fetchKMDetails":
		 
			qsDict['fileList'] = [ var for var in PluginFileSpace.query.filter_by(deleted = 0).join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginFileSpace.instance,PluginFileSpace.filesystem,PluginFileSpace.filesystemWarnThresh,PluginFileSpace.filesystemCriticalThresh,PluginFileSpace.inodeWarnThresh,PluginFileSpace.inodeCriticalThresh)]
			qsDict.move_to_end('fileList', last=False)
		  
			qs = PluginLog.query.filter_by(deleted = 0).join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).all()
			app.logger.info('%s Query log', qs)
			for rs in qs:
				logDict = {'instance':rs.instance,'logfile':rs.logfile,'noLogalarm':rs.noLogAlarm,'maxfilesize':rs.maxFileSize,'statefiletime':rs.statefileTime,'failoverfile':rs.failoverFile,'failovercommand':rs.failoverCommand,'patternDTOList':{'pattern':rs.pattern,'suppress':rs.suppress,'threshold':rs.threshold,'alarmsleep':rs.alarmsleep,'ignorecase':rs.ignorecase,'secPattern':rs.secPattern,'secBacklines':rs.secBacklines,'secFwdlines':rs.secFwdlines,'secPrint':rs.secPrint,'blackout':rs.blackout,'dedupType':rs.dedupType,'dedupIgnoreFields':rs.dedupIgnoreFields,'dedupDelim':rs.dedupDelim,'autoCmd':rs.autoCmd,'rewordTemplate':rs.rewordTemplate,'rewordDelim':rs.rewordDelim,'secnotfound':rs.secNotFound}}
				logList.append(logDict.copy())
			qsDict['logList'] = logList
			qsDict.move_to_end('logList', last=False)

			qsDict['mariadbList'] = [ var for var in PluginMariaDB.query.filter_by(deleted = 0).join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginMariaDB.instance,PluginMariaDB.port,PluginMariaDB.warningThreshold,PluginMariaDB.criticalThreshold)]
			qsDict.move_to_end('mariadbList', last=False)
		 
			
			qsDict['mysqlList'] = [ var for var in Pluginmysql.query.filter_by(deleted = 0).join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(Pluginmysql.instance,Pluginmysql.port,Pluginmysql.warningThreshold,Pluginmysql.criticalThreshold)]
			qsDict.move_to_end('mysqlList', last=False)

			qsDict['procList'] = [ var for var in PluginProc.query.filter_by(deleted = 0).join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginProc.instance,PluginProc.processString,PluginProc.minCount,PluginProc.maxCount,PluginProc.unixAccount,PluginProc.failoverCommand,PluginProc.failoverFile)]
			qsDict.move_to_end('procList', last=False)

			qsDict['runList'] = [ var for var in PluginRunScript.query.filter_by(deleted = 0).join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginRunScript.instance,PluginRunScript.script,PluginRunScript.interval)]
			qsDict.move_to_end('runList', last=False)
		elif api_method == "fetchRecoveryKMDetails":
			qsDict['fileList'] = [ var for var in PluginFileSpace.query.join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginFileSpace.instance,PluginFileSpace.filesystem,PluginFileSpace.filesystemWarnThresh,PluginFileSpace.filesystemCriticalThresh,PluginFileSpace.inodeWarnThresh,PluginFileSpace.inodeCriticalThresh)]
			qsDict.move_to_end('fileList', last=False)
		  
			qs = PluginLog.query.join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).all()
			
			for rs in qs:
				logDict = {'instance':rs.instance,'logfile':rs.logfile,'noLogalarm':rs.noLogAlarm,'maxfilesize':rs.maxFileSize,'statefiletime':rs.statefileTime,'failoverfile':rs.failoverFile,'failovercommand':rs.failoverCommand,'patternDTOList':{'pattern':rs.pattern,'suppress':rs.suppress,'threshold':rs.threshold,'alarmsleep':rs.alarmsleep,'ignorecase':rs.ignorecase,'secPattern':rs.secPattern,'secBacklines':rs.secBacklines,'secFwdlines':rs.secFwdlines,'secPrint':rs.secPrint,'blackout':rs.blackout,'dedupType':rs.dedupType,'dedupIgnoreFields':rs.dedupIgnoreFields,'dedupDelim':rs.dedupDelim,'autoCmd':rs.autoCmd,'rewordTemplate':rs.rewordTemplate,'rewordDelim':rs.rewordDelim,'secnotfound':rs.secNotFound}}
				logList.append(logDict.copy())
			qsDict['logList'] = logList
			qsDict.move_to_end('logList', last=False)

			qsDict['mariadbList'] = [ var for var in PluginMariaDB.query.join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginMariaDB.instance,PluginMariaDB.port,PluginMariaDB.warningThreshold,PluginMariaDB.criticalThreshold)]
			qsDict.move_to_end('mariadbList', last=False)
		 
			
			qsDict['mysqlList'] = [ var for var in Pluginmysql.query.join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(Pluginmysql.instance,Pluginmysql.port,Pluginmysql.warningThreshold,Pluginmysql.criticalThreshold)]
			qsDict.move_to_end('mysqlList', last=False)

			qsDict['procList'] = [ var for var in PluginProc.query.join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginProc.instance,PluginProc.processString,PluginProc.minCount,PluginProc.maxCount,PluginProc.unixAccount,PluginProc.failoverCommand,PluginProc.failoverFile)]
			qsDict.move_to_end('procList', last=False)

			qsDict['runList'] = [ var for var in PluginRunScript.query.join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginRunScript.instance,PluginRunScript.script,PluginRunScript.interval)]
			qsDict.move_to_end('runList', last=False)
		elif api_method == "fetchUrlDetails":
			qsDict['urlList'] = [ var for var in PluginUrl.query.filter_by(deleted = 0).join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginUrl.instance,PluginUrl.url,PluginUrl.searchString,PluginUrl.cspAuthentication)]
		elif api_method == "fetchRecoveryUrlDetails":
			qsDict['urlList'] = [ var for var in PluginUrl.query.join(Monitorgroup).filter(Monitorgroup.id.in_(Monitorgroup.query.join(Monitorgroup._monitoring_server_group).filter(Servergroup.id.in_(Server.query.filter_by(serverName = server_name).join(Server._server_group).values(Servergroup.id))).values(Monitorgroup.id))).values(PluginUrl.instance,PluginUrl.url,PluginUrl.searchString,PluginUrl.cspAuthentication)]
		else:
			qsDict['Error'] = "Err 0411 - method " + api_method + " does not exist"

		return jsonify(qsDict)
		
	except:
		qsDict['Error'] = "Please validate the request formate!"
		return jsonify(qsdict)