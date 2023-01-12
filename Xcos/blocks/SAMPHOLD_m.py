def SAMPHOLD_m(outroot, attribid, ordering, geometry, parameters):
    func_name = 'SAMPHOLD_m'

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName='samphold4_m',
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='d',
                      dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 1, parameters)

    return outnode


def get_from_SAMPHOLD_m(cell):
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
