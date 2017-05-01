import React from 'react'
import Navbar from 'COMPONENT/Navbar/'
import Footer from 'COMPONENT/Footer/'

let DevTools
if (__DEV__ && __COMPONENT_DEVTOOLS__) {
  // 组件形式的 Redux DevTools
  DevTools = require('COMPONENT/DevTools').default
}

const App = ({ children, location }) => (
  <div>
    <Navbar location={location} />
    { children }
    { DevTools && <DevTools /> }
    <Footer />
  </div>
)

export default App
