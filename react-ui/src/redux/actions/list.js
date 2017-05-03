import jobService from 'SERVICE/jobService'

const GET_ALL = 'GET_ALL'

const getList = (obj) => ({
  type: GET_ALL,
  payload: obj
})

const getAll = () => dispatch => {
    jobService.fetch().then(
      re => dispatch(getList(re))
    )
  }


export default {
  getAll
}

export const ACTION_HANDLERS = {
  // [GET_ALL]: (obj, { payload }) => {payload }
  [GET_ALL]: (msgs, { payload }) => payload
}
