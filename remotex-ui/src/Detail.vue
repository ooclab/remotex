<template>
  <div id="detail">
    <p>详情页</p>
    <!-- 详情页 -->

    <!-- loading -->
    <div v-if="detailLoading" style="display: -webkit-box; -webkit-box-pack:center; -webkit-box-align:center; height:200px;">
      <mu-circular-progress :size="40" :strokeWidth="5"/>
    </div>

    <!-- 详情 -->
    <template v-else class="">

      <!-- 卡片 -->
      <mu-card style="margin: 10px 20px 10px 20px;">
      
        <!-- 标题 / 来源 -->
        <mu-card-title :title="detail.title" :subTitle="detail.url"/>

        <!-- tags -->
        <mu-card-actions v-if="detail.categories" style="display: flex;">
          <template v-for="category in detail.categories">
            <mu-chip class="demo-chip" style="margin-left: 5px;">
              {{ category.name }}
            </mu-chip>
          </template>
        </mu-card-actions>

        <!-- 正文 -->
        <mu-card-text>
          {{ detail.body }}
        </mu-card-text>

        <!-- 价格 -->
        <mu-card-actions style="display: flex;">
          <p>报酬&nbsp;<b>{{ detail.price }}</b>&nbsp;元</p>
        </mu-card-actions>

        <!-- 其他 -->
        <mu-card-actions>

        <!-- 暂无用户注册及评论功能
          <mu-flat-button :label="detail.vote_up" class="demo-flat-button" icon="thumb_up"/>
          <mu-flat-button :label="detail.vote_down" class="demo-flat-button" icon="thumb_down"/>
        -->

          <p style="width: 33%">已发布&nbsp;<b>{{ detail.release_date }}</b>&nbsp;天</p>
          <p style="width: 33%">浏览&nbsp;<b>{{ detail.view_count }}</b>&nbsp;次</p>
          <p style="width: 33%">将于&nbsp;<b>{{ detail.expire_date }}</b>&nbsp;天后过期</p>
        </mu-card-actions>
        
      </mu-card>
    </template>

  </div>
</template>

<script>
import Vue from 'vue'
import App from './App.vue'

export default {
  name: 'detail',
  data () {
    return {
      detail: {},
      detailLoading: true
    }
  },
  created () {
    // 组件创建完后获取数据，
    // 此时 data 已经被 observed 了
    this.fetchData()
    console.log('detail')
  },
  watch: {
    // 如果路由有变化，会再次执行该方法
    '$route': 'fetchData'
  },
  methods: {
    fetchData () {
      this.detail = {}
      this.error = this.post = null
      this.detailLoading = true
      // replace getPost with your data fetching util / API wrapper
      Vue.http.get('https://remotex.ooclab.org/api/jobx/job/' + this.$route.params.id).then(response => {
        console.log(response)
        this.detail = response.body
        this.detailLoading = false
      }, response => {
        // console.log('error')
        this.detailLoading = false
      })
    }
  }
}
</script>

<style>
html, body {
  height: 100%;
}

#detail {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
  overflow: auto;
  -webkit-overflow-scrolling: touch;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}


</style>
