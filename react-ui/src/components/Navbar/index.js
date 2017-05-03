import React, { Component } from 'react'
import { connect } from 'react-redux'
import { IndexLink, Link } from 'react-router'
import LoginForm from './LoginForm'
import LogoutDropdown from './LogoutDropdown'

/* 导航栏全局显示，控制着用户的登录注销 */

@connect( // 功能同 UTIL/createContainer
  ({ userData }) => ({ userData }),
  require('ACTION/user').default
)
export default class Navbar extends Component {
  componentWillMount () {
    console.info('[Navbar] 初始化：检查用户是否已经登录')
    console.info('[TIPS] 由于有Redux Logger，故之后就不手动打印动作了')
    // this.props.checkLogin()
  }

  render() {
    return (
      <header className="r-header-warp">
        <div className="r-header-title">
          <h1>RemoteX&nbsp;快乐工作&nbsp;认真生活</h1>
        </div>
        <div className="r-header-sub">
          <h2>
            <span className="r-title">
              RemoteX&nbsp;远程工作空间
            </span>
            是一个开发远程/众包/外包信息聚合平台,我们将需求从不同的平台汇集到这里,非盈利组织运作。欢迎需求方/开发方联系我们。
          </h2>
        </div>
      </header>
    )
  }

  renderss () {
    let {
      userData, login, logout, // 通过 connect 获取
      location: { pathname }   // 通过 App 传入
    } = this.props

    return (
      <div className="row clearfix">
        <div className="col-md-12 column">
          <nav className="navbar navbar-default" role="navigation">
            <div className="navbar-header">
              <button
                type="button"
                className="navbar-toggle"
                data-toggle="collapse"
                data-target="#nav-collapse">
                <span className="sr-only">Toggle navigation</span>
                <span className="icon-bar"></span>
                <span className="icon-bar"></span>
                <span className="icon-bar"></span>
              </button>
              <Link to='/' className="navbar-brand">
                React Demo
              </Link>
            </div>
            <div className="collapse navbar-collapse" id="nav-collapse">
              <ul className="nav navbar-nav">
                <li className={pathname === '/' && 'active'}>
                  <IndexLink to='/'>
                    欢迎页
                  </IndexLink>
                </li>
                <li className={pathname.startsWith('/msg') && 'active'}>
                  <Link to='/msg'>
                    留言板
                  </Link>
                </li>
                <li className={pathname.startsWith('/todo') && 'active'}>
                  <Link to='/todo'>
                    待办事项(新功能)
                  </Link>
                </li>
              </ul>
              { userData ?
                <LogoutDropdown userData={userData} logout={logout} /> :
                <LoginForm login={login} />
              }
            </div>
          </nav>
        </div>
      </div>
    )
  }
}
