import jobService from 'SERVICE/jobService'

const GET_ALL = 'GET_ALL'

const getList = (obj) => ({
  type: GET_ALL,
  payload: obj
})

const getAll = (lm = 10, p = 1) => dispatch => {
    jobService.fetch(lm, p).then(
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
