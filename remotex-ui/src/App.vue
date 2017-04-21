<template>
  <div id="app">

    <!-- part 1 顶部 -->
    <mu-appbar title="Remotex - 自由汇聚于此">

      <!-- Slack icon -->   
      <mu-icon-button slot="right" href="https://remotex.slack.com/shared_invite/MTcwMDMxOTA4MjA5LTE0OTI1MTM1NTctMjY5MjhmMGZmMQ">
        <img src="./assets/Slack.png" />
      </mu-icon-button>

      <!-- GitHub icon -->
      <mu-icon-button slot="right" href="https://github.com/ooclab/remotex">
        <img style="width:24px; height:24px;" src="./assets/GitHub.png" />
      </mu-icon-button>
    </mu-appbar>

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
      <mu-tabs style="background:#424242;">
        <mu-tab style="color: #616161;" value="tab1" title="热门机会"/>
        <mu-tab style="color: #616161;" value="tab2" title="最新发布"/>
        <mu-tab style="color: #BDBDBD;" value="tab3" title="高薪报酬"/>
      </mu-tabs>
    </div>

    <!-- part 5 列表栏 -->
    <div >
      <mu-list>
          <mu-list-item>

            <!-- 循环体 -->
            <li v-for="item in list" class="page-infinite-listitem">

              <!-- 卡片 -->
              <mu-card style="margin: 10px 0 10px 0;">
                <mu-card-title :title="item.title" :subTitle="item.source"/>
                <mu-card-text>
                  {{ item.text }}
                </mu-card-text>
                <mu-card-actions style="display: flex;">
                  <p style="width: 33%">已发布 <b>{{ item.release }}</b> 天</p>
                  <p style="width: 33%">浏览 <b>{{ item.views }}</b> 次</p>
                  <p style="width: 33%">将于 <b>{{ item.expire }}</b> 天后过期</p>
                </mu-card-actions>
              </mu-card>
            </li>
          </mu-list-item>
      </mu-list>
    </div>
    <mu-infinite-scroll :scroller="scroller" :loading="loading" @load="loadMore"/>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      bottomSheet1: false,
      bottomSheet2: false,
      bottomSheet3: false,
      bottomSheet4: false,
      list: [
      {
        title: '「数码荔枝 lizhi.io」前端工程师',
        price: '7 ~ 10 K',
        source: 'yuancheng.work',
        tags: ['前端'],
        text: '岗位职责： 根据已有的平面设计图和原型，负责开发 PC 端 /移动端网站页面，类似： https://www.lizhi.io/blog/ 致力于不断改善用户浏览、支付体验，追求细节； 在代码交付前，可进行完整的自测；',
        release: 12,
        views: 155,
        expire: 8
      },
      {
        title: '薪传文化招福利向漫画主笔',
        price: '7 K',
        source: 'yuancheng.work',
        tags: ['前端'],
        text: '【岗位职责】根据分镜和剧本进行漫画线稿绘制能力要求，优秀的漫画绘画技巧和表现力，画工扎实，拥有鲜明独特的个人绘画风格更佳',
        release: 2,
        views: 52,
        expire: 18
      },
      {
        title: 'Java /前端工程师招聘',
        price: '15 ~ 20 K',
        source: 'yuancheng.work',
        tags: ['前端'],
        text: '我们团队有个项目正在进行中，现需要招募 2 个远程小伙伴。项目架构沿用之前的架构，是典型的微服务服架构，使用了 zookeeper, dubbo, spring 当后端技术，数据库采用： redis, MySQL ，一部分还使用 PHP 。第二期对部分系统会引入前后端分离的技术。使用 Angularjs 或 vue 。',
        release: 10,
        views: 35,
        expire: 10
      },
      {
        title: '「数码荔枝 lizhi.io」前端工程师',
        price: '7 ~ 10 K',
        source: 'yuancheng.work',
        tags: ['前端'],
        text: '岗位职责： 根据已有的平面设计图和原型，负责开发 PC 端 /移动端网站页面，类似： https://www.lizhi.io/blog/ 致力于不断改善用户浏览、支付体验，追求细节； 在代码交付前，可进行完整的自测；',
        release: 12,
        views: 155,
        expire: 8
      },
      {
        title: '薪传文化招福利向漫画主笔',
        price: '7 K',
        source: 'yuancheng.work',
        tags: ['前端'],
        text: '【岗位职责】根据分镜和剧本进行漫画线稿绘制能力要求，优秀的漫画绘画技巧和表现力，画工扎实，拥有鲜明独特的个人绘画风格更佳',
        release: 2,
        views: 52,
        expire: 18
      },
      {
        title: 'Java /前端工程师招聘',
        price: '15 ~ 20 K',
        source: 'yuancheng.work',
        tags: ['前端'],
        text: '我们团队有个项目正在进行中，现需要招募 2 个远程小伙伴。项目架构沿用之前的架构，是典型的微服务服架构，使用了 zookeeper, dubbo, spring 当后端技术，数据库采用： redis, MySQL ，一部分还使用 PHP 。第二期对部分系统会引入前后端分离的技术。使用 Angularjs 或 vue 。',
        release: 10,
        views: 35,
        expire: 10
      }],
      num: 10,
      loading: false,
      scroller: null
    }
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
    loadMore () {
      this.loading = true
      setTimeout(() => {
        for (let i = this.num; i < this.num + 10; i++) {
          this.list.push('item' + (i + 1))
        }
        this.num += 10
        this.loading = false
      }, 2000)
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
