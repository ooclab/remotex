<template>
  <div id="app">

    <!-- part 1 顶部 -->
    <mu-appbar title="RemoteX 快乐工作 认真生活">

      <!-- 右侧抽屉按钮 -->
      <mu-icon-button slot="right" icon="more_vert" @click="toggleDrawer(true)"/>
      
      <!-- Slack icon 
      <mu-icon-button slot="right" href="https://remotex.slack.com/shared_invite/MTcwMDMxOTA4MjA5LTE0OTI1MTM1NTctMjY5MjhmMGZmMQ" target="_blank">
        <img style="width:24px; height:24px;" src="./assets/Slack_White.png" />
      </mu-icon-button>--> 

      <!-- GitHub icon 
      <mu-icon-button slot="right" href="https://github.com/ooclab/remotex" target="_blank">
        <img style="width:24px; height:24px;" src="./assets/GitHub_White.png" />
      </mu-icon-button>-->
    </mu-appbar>

    <!-- part 1.1 抽屉 -->
    <mu-drawer right :open="openDrawer" :docked="docked" @close="toggleDrawer()">
      <mu-list @close="docked ? '' : toggleDrawer()">

        <!-- GitHub -->
        <mu-list-item title="GitHub" href="https://github.com/ooclab/remotex" target="_blank">
          <img style="width:24px; height:24px; position:absolute;left:15px;top:10px;" src="./assets/GitHub.png"/>
        </mu-list-item>

        <!-- Slack -->
        <mu-list-item title="Slack" href="https://remotex.slack.com/shared_invite/MTcwMDMxOTA4MjA5LTE0OTI1MTM1NTctMjY5MjhmMGZmMQ" target="_blank">
          <img style="width:24px; height:24px; position:absolute;left:15px;top:10px;" src="./assets/Slack.png"/>
        </mu-list-item>
        <mu-divider/>

        <!-- 关于 -->
        <mu-list-item title="About" href="https://github.com/ooclab/remotex" target="_blank">
          <mu-icon value="info" style="position:absolute;left:15px;top:10px;" />
        </mu-list-item>

        <!-- 联系 -->
        <mu-list-item title="Contact" href="https://github.com/ooclab/remotex" target="_blank">
          <mu-icon value="mail" style="position:absolute;left:15px;top:10px;"/>
        </mu-list-item>
        <mu-divider/>

        <!-- 关闭 -->
        <mu-list-item @click.native="openDrawer = false" title="Close">
          <mu-icon value="close" style="position:absolute;left:15px;top:10px;"/>
        </mu-list-item>
      </mu-list>
    </mu-drawer>

    <!-- part 2 搜索栏 -->
    <div>
      <mu-text-field style="width:60%;" hintText="输入关键词"/>
      <mu-flat-button label="搜索" class="demo-flat-button" icon="search" primary/>
    </div>

    <!-- part 3 类目栏 -->
    <div>
      <mu-raised-button style="width:40%; margin: 5px 5px 5px 0;" @click="openBottomSheet1" label="平台" icon="assignment_turned_in"/>

      <!-- 平台 -->
      <mu-bottom-sheet :open="bottomSheet1" @close="closeBottomSheet1">
        <mu-list @itemClick="closeBottomSheet1" style="height:200px">
          <mu-sub-header>
            请选择平台
          </mu-sub-header>
          <mu-list-item title="全部"/>
          <mu-list-item title="外包众包"/>
          <mu-list-item title="远程工作"/>
        </mu-list>
      </mu-bottom-sheet>

      <!-- 角色 -->
      <mu-raised-button style="width:40%; margin: 5px 0 5px 5px;" @click="openBottomSheet2" label="角色" icon="build"/>
      <mu-bottom-sheet :open="bottomSheet2" @close="closeBottomSheet2">
        <mu-list @itemClick="closeBottomSheet2" style="height:240px">
          <mu-sub-header>
            请选择角色
          </mu-sub-header>
          <mu-list-item title="全部"/>
          <mu-list-item title="项目管理"/>
          <mu-list-item title="产品经理"/>
          <mu-list-item title="设计"/>
          <mu-list-item title="开发"/>
          <mu-list-item title="测试"/>
          <mu-list-item title="运维"/>
          <mu-list-item title="市场"/>
          <mu-list-item title="运营"/>
        </mu-list>
      </mu-bottom-sheet>

      <!-- 工作 -->
      <mu-raised-button style="width:40%; margin: 5px 5px 5px 0;" @click="openBottomSheet3" label="工作" icon="devices"/>
      <mu-bottom-sheet :open="bottomSheet3" @close="closeBottomSheet3">
        <mu-list @itemClick="closeBottomSheet3" style="height:240px">
          <mu-sub-header>
            请选择工作
          </mu-sub-header>
          <mu-list-item title="全部"/>
          <mu-list-item title="Web 页面"/>
          <mu-list-item title="App 移动应用"/>
          <mu-list-item title="微信开发"/>
          <mu-list-item title="咨询"/>
        </mu-list>
      </mu-bottom-sheet>

      <!-- 城市 -->
      <mu-raised-button style="width:40%; margin: 5px 0 5px 5px;" @click="openBottomSheet4" label="城市" icon="location_city"/>
      <mu-bottom-sheet :open="bottomSheet4" @close="closeBottomSheet4">
        <mu-list @itemClick="closeBottomSheet4" style="height:240px">
          <mu-sub-header>
            请选择城市
          </mu-sub-header>
          <mu-list-item title="全部"/>
          <mu-list-item title="北京"/>
          <mu-list-item title="上海"/>
          <mu-list-item title="广州"/>
          <mu-list-item title="深圳"/>
          <mu-list-item title="杭州"/>
          <mu-list-item title="成都"/>
          <mu-list-item title="武汉"/>
          <mu-list-item title="南京"/>
          <mu-list-item title="西安"/>
          <mu-list-item title="厦门"/>
          <mu-list-item title="其他"/>
        </mu-list>
      </mu-bottom-sheet>
    </div>

    <!-- part 4 排序栏 -->
    <div>
      <!--<mu-tabs style="background:#424242;">-->
      <mu-tabs style="background:#ededed; margin-top: 10px;">
        <mu-tab style="color: #616161;" value="tab1" title="热门机会"/>
        <mu-tab style="color: #616161;" value="tab2" title="最新发布"/>
        <!--<mu-tab style="color: #BDBDBD;" value="tab3" title="高薪报酬"/>-->
        <mu-tab style="color: #F5193E;" value="tab3" title="高薪报酬"/>
      </mu-tabs>
    </div>

    <!-- part 5 列表栏 -->
    <div >
      <mu-list>

        <!-- 循环体 -->
        <template v-for="item in list" class="page-infinite-listitem">

          <!-- 卡片 -->
          <mu-card style="margin: 10px 0 10px 0;">

            <!-- 标题 / 来源 -->
            <mu-card-title :title="item.title" :subTitle="item.url"/>

            <!-- tags -->
            <mu-card-actions v-if="item.categories" style="display: flex;">
              <template v-for="category in item.categories">
                <mu-chip class="demo-chip" style="margin-left: 5px;">
                  {{ category.name }}
                </mu-chip>
              </template>
            </mu-card-actions>

            <!-- 正文 -->
            <mu-card-text>
              {{ item.body }}
            </mu-card-text>

            <!-- 价格 -->
            <mu-card-actions style="display: flex;">
              <p>报酬&nbsp;<b>{{ item.price }}</b>&nbsp;元</p>
            </mu-card-actions>

            <!-- 其他 -->
            <mu-card-actions style="display: flex;">

            <!-- 暂无用户注册及评论功能
              <mu-flat-button :label="item.vote_up" class="demo-flat-button" icon="thumb_up"/>
              <mu-flat-button :label="item.vote_down" class="demo-flat-button" icon="thumb_down"/>
            -->

              <p style="width: 33%">已发布&nbsp;<b>{{ item.release_date }}</b>&nbsp;天</p>
              <p style="width: 33%">浏览&nbsp;<b>{{ item.view_count }}</b>&nbsp;次</p>
              <p style="width: 33%">将于&nbsp;<b>{{ item.expire_date }}</b>&nbsp;天后过期</p>
            </mu-card-actions>
          </mu-card>
        </template>
      </mu-list>
    </div>
    <mu-infinite-scroll :scroller="scroller" :loading="loading" @load="loadMore"/>

    <!-- 底部 -->
    <p>总数 {{ total }}</p>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'app',
  data () {
    return {
      bottomSheet1: false,
      bottomSheet2: false,
      bottomSheet3: false,
      bottomSheet4: false,
      list: [],
      num: 10, // 每页显示个数
      loading: false, // 加载中图标
      scroller: null, // 页面上可滚动的元素
      total: 0, // 列表数据总数
      openDrawer: false, // 是否打开右侧抽屉
      docked: true //是否遮罩页面
    }
  },
  beforeMount() {
    Vue.http.get('https://remotex.ooclab.org/api/jobx/job').then(response => {
      console.log(response.data.data)
      this.list = response.data.data
      this.total = response.data.total
    }, response => {
      console.log('error')
    })
  },
  mounted () {
    this.scroller = this.$el
  },
  methods: {
    closeBottomSheet1 () {
      this.bottomSheet1 = false
    },
    openBottomSheet1 () {
      this.bottomSheet1 = true
    },
    closeBottomSheet2 () {
      this.bottomSheet2 = false
    },
    openBottomSheet2 () {
      this.bottomSheet2 = true
    },
    closeBottomSheet3 () {
      this.bottomSheet3 = false
    },
    openBottomSheet3 () {
      this.bottomSheet3 = true
    },
    closeBottomSheet4 () {
      this.bottomSheet4 = false
    },
    openBottomSheet4 () {
      this.bottomSheet4 = true
    },
    // 加载列表数据
    loadMore () {
      this.loading = true
      setTimeout(() => {
        for (let i = this.num; i < this.num + 10; i++) {
          this.list.push('item' + (i + 1))
        }
        this.num += 10
        this.loading = false
      }, 2000)
    },
    // 打开、关闭抽屉
    toggleDrawer (flag) {
      this.openDrawer = !this.openDrawer
      this.docked = !flag
    }
  }
}
</script>

<style>
html, body {
  height: 100%;
}

#app {
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

.page-infinite-listitem {
  /*height: 130px;*/
  line-height: 16px;
  text-align: left;
  display: block;
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
