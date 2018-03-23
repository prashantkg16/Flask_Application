from app import mysqldb

# helper table
servers_to_servergroup_table = mysqldb.Table('web_servers_servergroup', 
    mysqldb.Column("id", mysqldb.Integer, primary_key = True),
    mysqldb.Column('servers_id', mysqldb.Integer, mysqldb.ForeignKey('web_servers.id')), 
	mysqldb.Column('servergroups_id', mysqldb.Integer, mysqldb.ForeignKey('web_servergroups.id')))

monitorgroup_to_servergroup_table = mysqldb.Table('web_monitorgroup_servergroup', 
    mysqldb.Column("id", mysqldb.Integer, primary_key = True),
    mysqldb.Column('monitorgroup_id', mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id')), 
	mysqldb.Column('servergroups_id', mysqldb.Integer, mysqldb.ForeignKey('web_servergroups.id')))
	
# Define a base model for other database tables to inherit
class Base(mysqldb.Model):
    __abstract__  = True
    id            = mysqldb.Column(mysqldb.Integer, primary_key=True)

class Server(Base):
    __tablename__ = 'web_servers' 
    serverName = mysqldb.Column(mysqldb.String)    
    _server_group = mysqldb.relationship('Servergroup', backref='server_ref', lazy='dynamic', secondary=servers_to_servergroup_table)

class Servergroup(Base):
    __tablename__ = 'web_servergroups'
    serverGroupName = mysqldb.Column(mysqldb.String)
    _server = mysqldb.relationship('Server', secondary=servers_to_servergroup_table, backref=mysqldb.backref('servers_to_servergroup_table_backref', lazy='dynamic')) 

class Monitorgroup(Base): 
    __tablename__ = 'web_monitorgroup'
    monitorGroupName = mysqldb.Column(mysqldb.String)
    deleted = mysqldb.Column(mysqldb.SmallInteger)
    _monitoring_server_group = mysqldb.relationship('Servergroup', backref='monitor_group_server_ref', lazy='dynamic', secondary=monitorgroup_to_servergroup_table)
    _monitor_group_plugin_run = mysqldb.relationship('PluginRunScript')
    _monitor_group_plugin_mariadb = mysqldb.relationship('PluginMariaDB')

class PluginRunScript(Base):
    __tablename__ = 'nagios_pluginrunscript'
    monitorGroup_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id'))
    instance = mysqldb.Column(mysqldb.String)
    script = mysqldb.Column(mysqldb.TEXT)
    interval = mysqldb.Column(mysqldb.Float)
    deleted = mysqldb.Column(mysqldb.SmallInteger)

class PluginMariaDB(Base):
    __tablename__ = 'nagios_pluginmariadb'
    monitorGroup_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id'))
    instance = mysqldb.Column(mysqldb.String)
    warningThreshold = mysqldb.Column(mysqldb.String)
    criticalThreshold = mysqldb.Column(mysqldb.String)
    port = mysqldb.Column(mysqldb.Float)
    deleted = mysqldb.Column(mysqldb.SmallInteger)


class Pluginmysql(Base):
    __tablename__ = 'nagios_pluginmysql'
    monitorGroup_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id'))
    instance = mysqldb.Column(mysqldb.String)
    warningThreshold = mysqldb.Column(mysqldb.Float)
    criticalThreshold = mysqldb.Column(mysqldb.Float)
    port = mysqldb.Column(mysqldb.Float)
    deleted = mysqldb.Column(mysqldb.SmallInteger)

class PluginProc(Base):
    __tablename__ = 'nagios_pluginproc'
    monitorGroup_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id'))
    instance = mysqldb.Column(mysqldb.String)
    processString = mysqldb.Column(mysqldb.Text)
    minCount = mysqldb.Column(mysqldb.Float)
    maxCount = mysqldb.Column(mysqldb.Float)
    unixAccount = mysqldb.Column(mysqldb.Text)
    failoverFile = mysqldb.Column(mysqldb.Text)
    failoverCommand = mysqldb.Column(mysqldb.Text)
    deleted = mysqldb.Column(mysqldb.SmallInteger)

class PluginFileSpace(Base):
    __tablename__ = 'nagios_pluginfilespace'
    monitorGroup_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id'))
    instance = mysqldb.Column(mysqldb.String)
    filesystem = mysqldb.Column(mysqldb.String)
    filesystemWarnThresh = mysqldb.Column(mysqldb.Float)
    filesystemCriticalThresh = mysqldb.Column(mysqldb.Float)
    inodeWarnThresh = mysqldb.Column(mysqldb.Float)
    inodeCriticalThresh = mysqldb.Column(mysqldb.Float)
    deleted = mysqldb.Column(mysqldb.SmallInteger)

                      
class PluginLog(Base):
    __tablename__ = 'nagios_pluginlog'
    monitorGroup_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id'))
    instance = mysqldb.Column(mysqldb.String)
    logfile = mysqldb.Column(mysqldb.Text)
    noLogAlarm = mysqldb.Column(mysqldb.String)
    maxFileSize = mysqldb.Column(mysqldb.Float)
    statefileTime = mysqldb.Column(mysqldb.Float)
    failoverFile = mysqldb.Column(mysqldb.Text)
    failoverCommand = mysqldb.Column(mysqldb.Text)
    patternFlag = mysqldb.Column(mysqldb.Text)
    pattern = mysqldb.Column(mysqldb.String)
    patternValidator = mysqldb.Column(mysqldb.Text)
    suppress = mysqldb.Column(mysqldb.String)
    threshold = mysqldb.Column(mysqldb.String)
    alarmsleep = mysqldb.Column(mysqldb.Float)
    ignorecase = mysqldb.Column(mysqldb.String)
    secPattern = mysqldb.Column(mysqldb.String)
    secBacklines = mysqldb.Column(mysqldb.Float)
    secFwdlines = mysqldb.Column(mysqldb.Float)
    secNotFound = mysqldb.Column(mysqldb.String)
    secPrint = mysqldb.Column(mysqldb.String)
    blackout = mysqldb.Column(mysqldb.String)
    dedupType = mysqldb.Column(mysqldb.String)
    dedupIgnoreFields = mysqldb.Column(mysqldb.String)
    dedupDelim = mysqldb.Column(mysqldb.String)
    autoCmd = mysqldb.Column(mysqldb.Text)
    rewordTemplate = mysqldb.Column(mysqldb.String)
    rewordDelim = mysqldb.Column(mysqldb.String)
    deleted = mysqldb.Column(mysqldb.SmallInteger)


class PluginUrl(Base):
    __tablename__ = 'nagios_pluginurl'
    monitorGroup_id = mysqldb.Column(mysqldb.Integer, mysqldb.ForeignKey('web_monitorgroup.id'))
    instance = mysqldb.Column(mysqldb.String)
    url = mysqldb.Column(mysqldb.Text)
    searchString = mysqldb.Column(mysqldb.Text)
    cspAuthentication = mysqldb.Column(mysqldb.String)
    deleted = mysqldb.Column(mysqldb.SmallInteger)

