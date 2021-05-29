export default function ({ store, redirect }) {
  // eslint-disable-next-line no-console
  console.log('middleware2, token = ')
  // eslint-disable-next-line no-console
  console.log(store.state.token)
  if (store.state.token !== null) {
    return redirect('/main')
  }
}
