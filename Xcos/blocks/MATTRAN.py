def MATTRAN(outroot, attribid, ordering, geometry, parameters):
    func_name = 'MATTRAN'

    data_type = ['', 'mattran_m', 'matztran_m']
    para1 = int(parameters[0])
    para2 = int(parameters[1])

    if para2 == 2 and para1 == 2:
        simulation_func_name = 'mathermit_m'
    else:
        simulation_func_name = data_type[para1]

    outnode = addNode(outroot, BLOCK_BASIC,
                      **{'id': attribid},
                      ordering=ordering,
                      parent=1,
                      interfaceFunctionName=func_name,
                      simulationFunctionName=simulation_func_name,
                      simulationFunctionType='C_OR_FORTRAN',
                      style=func_name,
                      blockType='c',
                      dependsOnU=1)

    addExprsNode(outnode, TYPE_STRING, 2, parameters)

    return outnode


def get_from_MATTRAN(cell):
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
