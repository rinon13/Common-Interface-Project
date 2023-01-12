def CLKINV_f(outroot, attribid, ordering, geometry, parameters):
    func_name = 'CLKINV_f'

    outnode = addNode(outroot, BLOCK_EVENT_IN,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='input',
                      simulationFunctionType='DEFAULT',
                      style=func_name,
                      blockType='d')

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_CLKINV_f(cell):
    parameters = getParametersFromExprsNode(cell, TYPE_STRING)

    display_parameter = ''

    eiv = ''
    iiv = ''
    con = ''
    eov = ''
    iov = ''
    com = ''

    ports = [eiv, iiv, con, eov, iov, com]

    return (parameters, display_parameter, ports)
