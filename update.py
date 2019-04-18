import psycopg2
from configparser import ConfigParser
from argparse import ArgumentParser

def getArgs(argv=None):
    parser = ArgumentParser(description="Apply SQL file to all connections")

    parser.add_argument("-s", "--sql", dest="sqlfile",
                        help="SQL file to run", 
                        metavar="[SQLFILE]")
    parser.add_argument("-c", "--connections", dest="connfile",
                        help="the file that contains relevant DB credentials", 
                        metavar="[CONNECTIONFILE]")
    return parser.parse_args(argv)

def getConfig(connFile):
    with open(connFile) as cfg_file:
        config.read_file(cfg_file)  # read and parse entire file
    return config

def getSQL(sqlFile):
    return open(sqlFile, 'r')

def applySQL(config, sql):
    host,database = config['host'], config['database']
    user,password = config['user'], config['password']

    conn = psycopg2.connect(host=host, 
                            database=database, 
                            user=user, 
                            password=password)
    cursor = conn.cursor()
    cursor.execute(sql.read())

    [print("Notices: " + str(notice)) for notice in conn.notices]

def main(args):
    config = getConfig(args.connfile)
    sql = getSQL(args.sqlfile)
    [applySQL(config[section], sql) for section in config.sections()]

if __name__== "__main__":
    config = ConfigParser()
    args = getArgs()
    main(args)

