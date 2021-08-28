# plurals map to table.replace('_','-')
plurals = {
    'companies':'company',
    'departments':'department',
    'patterns' : 'patterns',
    'employees' : 'employee'
}


@request.restful()
def v1():
    import json;
    import logging
    response.view = 'generic.' + request.extension

    def GET(*args, **vars):

        if len(args)>0 and args[0] not in plurals.keys():
            return dict(status="fail",data='no matching pattern, use plural')

         # map plurals to table
        if len(args)>0 and args[0] in  plurals.keys():
            t  = tuple([plurals[a] if a.replace('_','-') in plurals.keys() else a  for a in args])
            args = t

        # use pre defined patterns
        patterns = 'auto'

        parser = db.parse_as_rest(patterns, args, vars)

        if parser.status == 200:
            return dict(status="success",data=parser.response)
        else:
            return dict(status="fail",data=parser.error)

        return dict(status='fail')

    def POST(table_name,*args, **vars):
        response.view = 'generic.' + request.extension

        if len(args)>0 and args[0] not in plurals.keys():
            return dict(status="fail",data='no matching pattern, use plural')

        if table_name in plurals.keys():
            table_name = plurals[table_name].replace('_','-')
        
        # check id if included in parameters
        id = int(vars['id'] or 0) if 'id' in vars else 0

        try:
            # if included
            if id > 0: 
                result = db(db[table_name].id == id).validate_and_update(**vars)
                if 'updated' in result:
                    return dict(status="success", data=result)
                else:
                    return dict(status="fail", data=result)
            else:
                result = db[table_name].validate_and_insert(**vars)
                if (('id' in result) and (int(result['id'] or 0) > 0)):
                    return dict(status="success", data=result)
                else:
                    return dict(status="fail", data=result)
        except:
             return dict(status="fail", message=T('SERVER OR DATABASE ERROR'))
    
    def PUT(table_name,*args, **vars):
        response.view = 'generic.' + request.extension

        if len(args)>0 and args[0] not in plurals.keys():
            return dict(status="fail",data='no matching pattern, use plural')

        if table_name in plurals.keys():
            table_name = plurals[table_name].replace('_','-')
        
        # check id if included in parameters
        id = int(vars['id'] or 0) if 'id' in vars else 0
        if id == 0:
             return dict(status="fail", message=T('Record ID is required'))

        try:
            result = db(db[table_name].id == id).validate_and_update(**vars)
            if 'updated' in result:
                return dict(status="success", data=result)
            else:
                return dict(status="fail", data=result)
        except:
             return dict(status="fail", message=T('SERVER OR DATABASE ERROR'))
    
    def DELETE(table_name,*args):
        response.view = 'generic.' + request.extension

        if table_name not in plurals.keys():
            return dict(status="fail",data='no matching pattern, use plural')

        if table_name in plurals.keys():
            table_name = plurals[table_name].replace('_','-')
        
        # check id if included in parameters
        id = int(args[0] or 0) if len(args) else 0
        if id == 0:
             return dict(status="fail", message=T('Record ID is required'))

        try:
            result = db(db[table_name].id == id).delete()
            return dict(status="success", data=result)
            
        except:
             return dict(status="fail", message=T('SERVER OR DATABASE ERROR'))
                

    return locals()