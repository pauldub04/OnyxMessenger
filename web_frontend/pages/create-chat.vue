<template>
  <v-row no-gutters>
    <NavigationDrawer
      :username="$store.state.user.username"
      :email="$store.state.user.email"
    ></NavigationDrawer>
    <v-col justify="center">
      <v-container>
        <h1>{{ $t('pages.createChat.label') }}</h1>
        <v-stepper v-model="stepper" class="mt-5" vertical>
          <v-stepper-step :complete="stepper > 1" step="1">
            {{ $t('pages.createChat.stepOne.stepLabel') }}
          </v-stepper-step>
          <v-stepper-content step="1">
            <v-card flat>
              <v-radio-group v-model="newChatType" class="ml-2">
                <v-radio
                  :label="$t('pages.createChat.stepOne.privateMessages')"
                  :value="1"
                ></v-radio>
                <v-radio
                  :label="$t('pages.createChat.stepOne.groupChat')"
                  :value="2"
                ></v-radio>
              </v-radio-group>
            </v-card>
            <v-btn
              :disabled="newChatType === null"
              color="primary"
              @click="stepper = 2"
            >
              {{ $t('pages.createChat.continue') }}
            </v-btn>
            <v-btn text to="/main">
              {{ $t('pages.createChat.cancel') }}
            </v-btn>
          </v-stepper-content>
          <v-stepper-step :complete="stepper > 2" step="2">
            {{ $t('pages.createChat.stepTwo.stepLabel') }}
          </v-stepper-step>
          <v-stepper-content step="2">
            <v-container v-if="newChatType === 1">
              <v-autocomplete
                :items="users"
                v-model="inviteUserName"
                class="mt-4 mr-5"
                :placeholder="$t('pages.createChat.stepTwo.placeholderOne')"
                clearable
                :label="$t('pages.createChat.stepTwo.placeholderOne')"
              ></v-autocomplete>
            </v-container>
            <v-container v-else>
              <v-autocomplete
                :items="users"
                v-model="inviteUserName"
                chips
                deletable-chips
                multiple
                class="mt-4 mr-5"
                :placeholder="$t('pages.createChat.stepTwo.placeholderTwo')"
                clearable
                :label="$t('pages.createChat.stepTwo.placeholderTwo')"
              ></v-autocomplete>
            </v-container>
            <v-btn
              color="primary"
              @click="createChat"
              v-if="newChatType == 1"
              :disabled="inviteUserName === null"
            >
              {{ $t('pages.createChat.createChat') }}
            </v-btn>
            <v-btn color="primary" @click="stepper = 3" v-else>
              {{ $t('pages.createChat.continue') }}
            </v-btn>
            <v-btn text @click="stepper = 1">
              {{ $t('pages.createChat.cancel') }}
            </v-btn>
          </v-stepper-content>

          <div v-if="newChatType == 2">
            <v-stepper-step :complete="stepper > 3" step="3">
              {{ $t('pages.createChat.chatName') }}
            </v-stepper-step>
            <v-stepper-content step="3">
              <v-form v-model="valid">
                <v-text-field
                  :label="$t('pages.createChat.createChat')"
                  v-model="chatName"
                  :rules="[
                    (v) => !!v || $t('pages.createChat.stepThree.titleRules'),
                  ]"
                  required
                  clearable
                ></v-text-field>
                <v-btn color="primary" @click="createChat" :disabled="!valid">
                  {{ $t('pages.createChat.createChat') }}
                </v-btn>
                <v-btn text @click="stepper = 1">
                  {{ $t('pages.createChat.cancel') }}
                </v-btn>
              </v-form>
            </v-stepper-content>
          </div>
        </v-stepper>
      </v-container>
    </v-col>
  </v-row>
</template>

<script>
import NavigationDrawer from '~/components/NavigationDrawer'
export default {
  name: 'CreateChat',
  components: { NavigationDrawer },
  data: () => ({
    stepper: 1,
    newChatType: null,
    inviteUserName: null,
    chatName: null,
    users: [],
    chatType: [
      {
        name: 'Личные сообщения',
        val: 1,
      },
      {
        name: 'Групповой чат',
        val: 2,
      },
    ],

    valid: false,
  }),
  created() {
    this.getUsers()
  },
  mounted() {
    this.$store.dispatch('setTheme', this.$i18n)
  },
  methods: {
    createChat() {
      if (this.newChatType === 1) {
        this.chatName = this.inviteUserName

        const tmp = this.inviteUserName
        this.inviteUserName = []
        this.inviteUserName.push(tmp)
      }
      console.log(this.newChatType)
      console.log(this.inviteUserName)
      console.log(this.chatName)

      this.$axios
        .post('http://localhost:8000/api/chats/', {
          type: this.newChatType,
          users: this.inviteUserName,
          title: this.chatName,
        })
        .then((response) => {
          console.log(response.data)
          this.$router.push('/main')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getUsers() {
      this.$axios
        .get(`http://127.0.0.1:8000/api/users/all/`)
        .then((response) => {
          this.users = response.data.users
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
