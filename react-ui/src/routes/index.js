import { injectReducer } from 'REDUCER'
import createContainer from 'UTIL/createContainer'

export default {
  path: '/',

  component: require('COMPONENT/App').default,
  
  indexRoute: {
    getComponent (nextState, cb) {
      require.ensure([], (require) => {
        injectReducer('list', require('REDUCER/list').default)
        const getPageContainer = createContainer(
          ({ pages }) => ({ pages }),
          require('ACTION/list').default,
          require('COMPONENT/index/').default
        )

        cb(null, getPageContainer)
      }, 'pages')
    }
  },
  
  childRoutes: [
    { path: 'redirect', component: require('COMPONENT/Redirect').default },
    { path: '*', component: require('COMPONENT/404').default }
  ]
}
