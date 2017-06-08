import createReducer from 'UTIL/createReducer'
import { ACTION_HANDLERS } from 'ACTION/list'
import initState from 'STORE/initState'

export default createReducer(initState.list, ACTION_HANDLERS)
