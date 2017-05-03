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
        data = []
      }
    } = this.props

    return (
      <div className="r-container">
      {
        data.map((item, k) => {
          return (
            <Item data={item}/>
          )
        })
      }
      <Pagination />
      </div>
    )
  }
}
