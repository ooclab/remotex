<template>
  <div id="app">
    <mt-header fixed title="RemoteX — 自由汇聚于此"></mt-header>

    <!-- 搜索 -->
    <div id="div_search">
      <input id="input_search" type="search" placeholder="输入关键词"/>
      <mt-button id="button_search">
        <img src="./assets/ic_search.png" height="16" width="16" slot="icon">
        搜索
      </mt-button>
    </div>

    <!-- 类目 -->
    <div id="div_category">
      <div style="width:25%;" @click="openPlatformDockPopup($event)">
        <img src="./assets/ic_assignment.png" height="24" width="24">
        <div>平台</div>
      </div>
      <mt-popup v-model="platformDockPopupVisible" position="bottom" class="popup">
        <div class="popup-btn-div">
          <mt-cell class="popup-btn popup-btn-left" @click.native="closeDockPopup" title="取消"></mt-cell>
          <mt-cell class="popup-btn popup-btn-right" @click.native="pickDockValue" title="确认"></mt-cell>
          <mt-cell class="popup-btn-null"></mt-cell>
        </div>
        <mt-picker :slots="platformSlots" @change="onDockValuesChange" :visible-item-count="5" :show-toolbar="false">
        </mt-picker>
      </mt-popup>
      <div style="width:25%;" @click="openRoleDockPopup($event)">
        <img src="./assets/ic_build.png" height="24" width="24">
        <div>工作</div>
      </div>
      <mt-popup v-model="roleDockPopupVisible" position="bottom" class="popup">
        <div class="popup-btn-div">
          <mt-cell class="popup-btn popup-btn-left" @click.native="closeDockPopup" title="取消"></mt-cell>
          <mt-cell class="popup-btn popup-btn-right" @click.native="pickDockValue" title="确认"></mt-cell>
          <mt-cell class="popup-btn-null"></mt-cell>
        </div>
        <mt-picker :slots="roleSlots" @change="onDockValuesChange" :visible-item-count="5" :show-toolbar="false">
        </mt-picker>
      </mt-popup>
      <div style="width:25%" @click="openWorkDockPopup($event)">
        <img src="./assets/ic_devices.png" height="24" width="24">
        <div>任务</div>
      </div>
      <mt-popup v-model="workDockPopupVisible" position="bottom" class="popup">
        <div class="popup-btn-div">
          <mt-cell class="popup-btn popup-btn-left" @click.native="closeDockPopup" title="取消"></mt-cell>
          <mt-cell class="popup-btn popup-btn-right" @click.native="pickDockValue" title="确认"></mt-cell>
          <mt-cell class="popup-btn-null"></mt-cell>
        </div>
        <mt-picker :slots="workSlots" @change="onDockValuesChange" :visible-item-count="5" :show-toolbar="false">
        </mt-picker>
      </mt-popup>
      <div style="width:25%" @click="openCityDockPopup($event)">
        <img src="./assets/ic_city.png" height="24" width="24">
        <div>城市</div>
      </div>
      <mt-popup v-model="cityDockPopupVisible" position="bottom" class="popup">
        <div class="popup-btn-div">
          <mt-cell class="popup-btn popup-btn-left" @click.native="closeDockPopup" title="取消"></mt-cell>
          <mt-cell class="popup-btn popup-btn-right" @click.native="pickDockValue" title="确认"></mt-cell>
          <mt-cell class="popup-btn-null"></mt-cell>
        </div>
        <mt-picker :slots="citySlots" @change="onDockValuesChange" :visible-item-count="5" :show-toolbar="false">
        </mt-picker>
      </mt-popup>
    </div>

    <!-- 排序 -->
    <div id="div_sorts">
      <div style="width:33%">
        热门机会
      </div>
      <div style="width:33%">
        最新发布
      </div>
      <div style="width:33%">
        高薪报酬
      </div>
    </div>

    <!-- 列表 -->
    <div id="div_list">
      <ul class="page-infinite-list" v-infinite-scroll="loadMore" infinite-scroll-disabled="loading" infinite-scroll-distance="50">
        <li v-for="item in list" class="page-infinite-listitem">
          <p>标题 <b>{{ item.title }}</b></p>
          <p>来源 <b>{{ item.source }}</b></p>
          <p>正文 <b>{{ item.text }}</b></p>
          <div style="display: flex;">
            <p style="width: 33%">已发布 <b>{{ item.release }}</b> 天</p>
            <p style="width: 33%">浏览 <b>{{ item.views }}</b> 次</p>
            <p style="width: 33%">将于 <b>{{ item.expire }}</b> 天后过期</p>
          </div>
        </li>
      </ul>
    </div>

    <!-- Loading -->
    <p v-show="loading" class="page-infinite-loading">
      <mt-spinner type="fading-circle"></mt-spinner>
      加载中...
    </p>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      loading: false, // order list 加载中
      platformDockPopupVisible: false,
      roleDockPopupVisible: false,
      workDockPopupVisible: false,
      cityDockPopupVisible: false,
      platformSlots: [ 
        {
          flex: 1,
          values: ['全部', '众包外包', '远程工作'],
          className: 'slot1',
          textAlign: 'center'
        }
      ],
      roleSlots: [ 
        {
          flex: 1,
          values: ['全部', '项目管理', '产品经理', '设计', '开发', '测试', '运维'],
          className: 'slot2',
          textAlign: 'center'
        }
      ],
      workSlots: [ 
        {
          flex: 1,
          values: ['全部', 'Website', 'App', '微信开发', 'HTML5', '咨询'],
          className: 'slot3',
          textAlign: 'center'
        }
      ],
      citySlots: [ 
        {
          flex: 1,
          values: ['全部', '北京', '上海', '广州', '深圳', '杭州', '成都', '南京', '武汉', '西安', '厦门', '其他'],
          className: 'slot4',
          textAlign: 'center'
        }
      ],
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
      }]
    }
  },
  methods: {
    startHacking () {
      this.$toast('It Works!')
    },
    loadMore() {
      this.loading = true;
      setTimeout(() => {
        let last = this.list[this.list.length - 1];
        for (let i = 1; i <= 10; i++) {
          this.list.push(last + i);
        }
        this.loading = false;
      }, 2500);
    },
    openPlatformDockPopup() {
      this.platformDockPopupVisible = true
    },
    openRoleDockPopup() {
      this.roleDockPopupVisible = true
    },
    openWorkDockPopup() {
      this.workDockPopupVisible = true
    },
    openCityDockPopup() {
      this.cityDockPopupVisible = true
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#input_search {
  width: 60%;
  height: 30px;
  border-radius: 25px;
  border: 1px solid #dbdbdb;
  padding-left: 20px;
}

#button_search {
  margin-left: 5px;
  height: 30px;
}

#div_category {
  display: flex;
  text-align: center;
  margin: 10px 0 10px 0;
}

#div_sorts {
  display: flex;
  height: 30px;
  background: #DBDBDB;
  margin: 10px 0 10px 0;
  padding-top: 10px;
}

.page-infinite-listitem {
  /*height: 130px;*/
  line-height: 16px;
  text-align: left;
  border-bottom: 1px solid #eee;
  display: block;
}

.page-infinite-loading {
  text-align: center;
  height: 50px;
  line-height: 50px;
}  
.page-infinite-loading div {
  display: inline-block;
  vertical-align: middle;
  margin-right: 5px;
}

.popup {
  width: 100%;
}

.popup-btn-div {
  display:-moz-box; /* Firefox */
  display:-webkit-box; /* Safari and Chrome */
  display:box;
}

.popup-btn {
  -moz-box-flex:1.0; /* Firefox */
  -webkit-box-flex:1.0; /* Safari and Chrome */
  box-flex:1.0;
}

.popup-btn-left {
  text-align: left;
  margin-left:20px;
}

.popup-btn-right {
  text-align: right;
  margin-right:20px;
}

.popup-btn-null {
  width: 0;
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
