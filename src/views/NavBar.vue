<template>
  <b-navbar id="navbar-nav" toggleable="md" variant="primary" type="dark">
    <b-container>
      <b-navbar-brand href="/">
        <font-awesome-icon size="lg" class="mr-1" :icon="['traink', 'logo']" />
        <b>Train<span class="text-theme">K</span></b>
      </b-navbar-brand>
      <b-button-group class="d-md-none">
        <b-button variant="outline-light" :href="user ? '/user/setting' : '/user/session/'">
          <font-awesome-icon icon="user-circle" size="lg" />
        </b-button>
        <b-button :variant="expanded ? 'light' : 'outline-light'" aria-controls="collapse" :aria-expanded="expanded" @click="expanded = !expanded">
          <font-awesome-icon icon="bars" />
        </b-button>
      </b-button-group>
      <b-collapse is-nav id="nav-collapse" v-model="expanded" class="justify-content-end">
        <b-navbar-nav>
          <b-nav-item :to="{name:'Ticket-Home'}" :active="location === 'ticket'"><font-awesome-icon icon="ticket-alt"></font-awesome-icon>购票</b-nav-item>
          <b-nav-item href="/info" :active="location === 'info'"><font-awesome-icon icon="info-circle" />查询</b-nav-item>
          <b-nav-item disabled href="#"><font-awesome-icon icon="briefcase" />通勤</b-nav-item>
          <b-nav-item :to="{name:'Map'}" :active="location === 'map'"><font-awesome-icon icon="map" />地图</b-nav-item>
          <b-nav-item disabled href="/forum" :active="location === 'forum'"><font-awesome-icon icon="comments" />社区</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
      <b-button id="navbar-popover-trigger" :variant="userPopoverShown ? 'light' : 'outline-light'" class="ml-3 d-none d-md-block">
        <font-awesome-icon icon="user-circle" size="lg" />
      </b-button>
      <b-popover
        container="navbar"
        target="navbar-popover-trigger"
        triggers="click"
        placement="bottomleft"
        @show="userPopoverShown=true"
        @hide="userPopoverShown=false">
        <glimpse v-if="user" />
        <login-view class="m-4" v-else />
      </b-popover>
    </b-container>
  </b-navbar>
</template>

<script>
import LoginView from '@/components/user/Login'
import Glimpse from '@/components/user/Glimpse'
import { states } from '@/store/auth'
import {
  faTrain,
  faBars,
  faUserCircle,

  faTicketAlt,
  faInfoCircle,
  faBriefcase,
  faMap,
  faComments
} from '@fortawesome/fontawesome-free-solid'
import { MainLogo } from '@/assets/Logo'
import fontawesome from '@fortawesome/fontawesome'
fontawesome.library.add(faTrain, faBars, faUserCircle)
fontawesome.library.add(faTicketAlt, faInfoCircle, faBriefcase, faMap, faComments)
fontawesome.library.add(MainLogo)

export default {
  props: {
    authenticated: Boolean,
    id: Number,
    email: String,
    hash: String,
    username: String,
    firstname: String,
    lastname: String
  },
  data () {
    return {
      userPopoverShown: false,
      expanded: false
    }
  },
  mounted () {
    if (this.authenticated) {
      this.$store.commit('auth/login', {
        'email': this.email,
        'hash': this.hash,
        'username': this.username,
        'first_name': this.firstname,
        'last_name': this.lastname,
        'id': this.id
      })
    } else this.$store.commit('auth/logout')
  },
  methods: {
    location: () => window.location.pathname.split('/')[1]
  },
  computed: states,
  components: { LoginView, Glimpse }
}
</script>

<style lang="scss">
#nav-collapse svg {
  margin-right: 0.25rem;
}
#navbar .popover {
  width: 276px;
  .popover-body {
    padding: 0 !important;
  }
}
</style>
