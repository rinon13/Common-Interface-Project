import api from '../../utils/Api'
import * as actions from './actions'

// Actions for listing stored component properites on double click on component
export const getCompProperties = (id) => (dispatch) => {
  const url = 'block_parameters/?block=' + parseInt(id)
  api.get(url)
    .then(
      (res) => {
        dispatch({
          type: actions.GET_COMP_PROPERTIES,
          payload: {
            id: id,
            compProperties: res.data
          }
        })
      }
    )
    .catch((err) => { console.error(err) })
}

// Actions for updating entered component properites on clicking set parameters
export const setCompProperties = (id, compProperties) => (dispatch) => {
  dispatch({
    type: actions.SET_COMP_PROPERTIES,
    payload: {
      id: id,
      compProperties: compProperties
    }
  })
}

// Handeling hiding of component properties sidebar
export const closeCompProperties = () => (dispatch) => {
  dispatch({
    type: actions.CLOSE_COMP_PROPERTIES
  })
}
