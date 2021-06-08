import React, { useState, useContext } from 'react'
import { fade } from '@material-ui/core/styles'

import theme from '../../styles/theme'
import { UserEmailContext } from '../../src/contexts/userEmailContext'

import RegisterDialog from './RegisterDialog'

const EmailField = () => {
  const { userEmail } = useContext(UserEmailContext)
  const [registerDialogOpen, setRegisterDialogOpen] = useState(false)

  return (
    <>
      <button
        style={{
          cursor: 'pointer',
          backgroundColor: fade(theme.palette.common.white, 0.15),
          color: theme.palette.common.white,
          borderRadius: 4,
          padding: theme.spacing(1, 2),
          border: 'none',
        }}
        onClick={(e) => {
          setRegisterDialogOpen(true)
        }}
      >
        <span style={{ color: 'inherit', fontSize: '1.1em' }}>
          {userEmail || 'Enter your email'}
        </span>
      </button>
      <RegisterDialog
        open={registerDialogOpen}
        onClose={() => {
          setRegisterDialogOpen(false)
        }}
      />
    </>
  )
}

export default EmailField
