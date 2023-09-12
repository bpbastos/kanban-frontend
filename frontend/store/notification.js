import { defineStore } from 'pinia'

export const useNotificationStore = defineStore('notification', () => {
    const notifications = ref([])

    function info(m) {
        const d = new Date()
        const tempNot = {
          type: 'info',
          text: m,
          date: d.toISOString()
        }     
        this.notifications.unshift(tempNot)
    }
    function success(m) {
        const d = new Date()    
        const tempNot = {
          type: 'success',
          text: m,
          date: d.toISOString()
        }   
        this.notifications.unshift(tempNot)
    }
    function warning(m) {
        const d = new Date()    
        const tempNot = {
          type: 'warning',
          text: m,
          date: d.toISOString()
        }   
        this.notifications.unshift(tempNot)
    }  
    function error(m) {
        const d = new Date()    
        const tempNot = {
          type: 'error',
          text: m,
          date: d.toISOString()
        }   
        this.notifications.unshift(tempNot)
    }

    function getLastNotification() {
      return this.notifications[0]
    }

    return { info, success, warning, error, notifications, getLastNotification }

})