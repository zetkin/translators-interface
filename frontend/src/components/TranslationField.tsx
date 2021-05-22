import React, { useState, ChangeEvent } from 'react'
import { Button, TextField } from '@material-ui/core'

import { Translation, TranslationPostBody } from '../global.types'
import { postTranslation } from '../api/translations'

interface Props {
  base: Translation
  selected: Translation
}

const TranslationField = ({ base, selected }: Props) => {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string>()
  const [saveSuccess, setSaveSuccess] = useState(false)
  const [savedValue, setSavedValue] = useState<string>(selected?.text)
  const [value, setValue] = useState<string>(selected?.text)

  console.log(value != savedValue)

  const handleSave = async () => {
    setError(null)
    setSaveSuccess(false)
    setLoading(true)

    // Build request body
    const body: TranslationPostBody = {
      ...base,
      author: 'river',
      from_repository: false,
      language: selected.language.id,
      file_path: selected.file_path,
      text: value,
      created_at: new Date(),
    }

    try {
      const resBody = await postTranslation(body)
      setLoading(false)
      setSaveSuccess(true)
      setSavedValue(resBody.text)
    } catch (e) {
      setLoading(false)
      setError('Could not save')
      console.error('Error posting!')
    }
  }

  return (
    <div style={{ display: 'flex' }}>
      <TextField
        multiline
        color="secondary"
        error={error != null}
        label={error || null}
        style={{
          width: '100%',
        }}
        variant="outlined"
        defaultValue={savedValue}
        onInput={(e: ChangeEvent<HTMLInputElement>) => {
          e.preventDefault()
          setSaveSuccess(false)
          setError(null)
          setValue(e.target.value)
        }}
      />
      {
        // If current value different than saved value
        value != savedValue ||
        // If request in process
        loading ||
        // If reqest successful
        saveSuccess ? (
          <Button
            disabled={loading || saveSuccess}
            style={{ marginLeft: '5px' }}
            variant="contained"
            color="secondary"
            disableElevation
            onClick={handleSave}
          >
            {saveSuccess ? '✓' : loading ? '...' : 'Save'}
          </Button>
        ) : null
      }
    </div>
  )
}

export default TranslationField
