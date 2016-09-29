
def log(msg, *args, **kwargs):
    level = kwargs.get('level', 'info')
    print '%s.log > %s' % (level, msg % args)

log('Hi :)')
log('Care!', level='warning')
log('PARAMS!! %s, asdasd %s, DATA: %s', 'var1', 'var2', 'var3', level='error')
