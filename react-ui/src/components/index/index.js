import React, { Component } from 'react'
import Item from 'COMPONENT/Item'
import Pagination from 'COMPONENT/Pagination'
import { connect } from 'react-redux'

@connect(
          ({ list }) => ({ list }),
          require('ACTION/list').default
)
export default class Index extends Component {
  constructor (props, context) {
    super(props, context)
  }

  componentWillMount() {
    this.props.getAll()
  }

  render() {
    const {
      list: {
        data = [],
        total,
        filter = []
      }
    } = this.props

    return (
      <div className="r-container">
      <h3 className="r-panel-title">工作机会</h3>
      {
        data.map((item, k) => {
          return (
            <Item data={item}/>
          )
        })
      }
      <Pagination filter={filter} total={total} {...this.props}/>
      </div>
    )
  }
}
