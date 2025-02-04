def ExplicitOutputPort(outroot, attribid, parentattribid, ordering, geometry,
                       addDataLines=False, value='', forSplitBlock=False):
    func_name = 'ExplicitOutputPort'

    if forSplitBlock:
        outnode = addNode(outroot, func_name, connectable=0,
                          dataType='UNKNOW_TYPE', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, visible=0)
    elif addDataLines:
        outnode = addNode(outroot, func_name, dataColumns=1, dataLines=1,
                          dataType='REAL_MATRIX', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, value=value)
    else:
        outnode = addNode(outroot, func_name, dataColumns=1,
                          dataType='REAL_MATRIX', **{'id': attribid},
                          ordering=ordering, parent=parentattribid,
                          style=func_name, value=value)

    addNode(outnode, 'mxGeometry', **{'as': 'geometry'},
            height=geometry['height'], width=geometry['width'],
            x=geometry['x'], y=geometry['y'])

    return outnode


def addExplicitOutputPortForSplit(outroot, splitBlock, sourceVertex, targetVertex,
                                  sourceType, targetType, edgeDict, inputCount,
                                  outputCount, nextAttrib, nextAttribForSplit):
    outputCount += 1
    geometry = {}
    geometry['width'] = 8
    geometry['height'] = 8
    geometry['x'] = 7
    geometry['y'] = -4
    ExplicitOutputPort(outroot, nextAttrib, splitBlock, outputCount, geometry,
                       forSplitBlock=True)
    edgeDict[nextAttribForSplit] = ('ExplicitLink', nextAttrib, targetVertex,
                                    'ExplicitOutputPort', targetType)
    nextAttrib += 1
    nextAttribForSplit += 1
    return (inputCount, outputCount, nextAttrib, nextAttribForSplit)
