import { GetServerSideProps, NextPage } from 'next'
import Head from 'next/head'
import NextLink from 'next/link'

import {
  Container,
  Typography,
  Card,
  Breadcrumbs,
  Link,
} from '@material-ui/core'

import { COUNTRIES } from '../../../src/constants'
import { Project } from '../../../src/global.types'
import { getProject, getProjects } from '../../../src/api/projects'

/**
 * Project Page - List project's languages
 */

interface StaticProps {
  project: Project
}

type QueryParams = {
  id: string
}

export const getServerSideProps: GetServerSideProps<StaticProps, QueryParams> = async ({
  params,
}) => {
  const project = await getProject(params.id)
  const projectWithoutEnglish: Project = {
    ...project,
    languages: [
      ...project.languages.filter(
        (language) => language.language_code !== 'en'
      ),
    ],
  }
  return { props: { project: projectWithoutEnglish } }
}

const ProjectPage: NextPage<StaticProps> = ({ project }) => {
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta
          name="description"
          content="Contribute to the localisation of Zetkin's software"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container style={{ marginTop: 20, marginBottom: 20 }}>
          {/* Breadcrumbs */}
          <Breadcrumbs style={{ marginBottom: 20 }} aria-label="breadcrumb">
            <Link color="inherit" href="/">
              Projects
            </Link>
            <Typography color="textPrimary">{project.name}</Typography>
          </Breadcrumbs>

          {/* Header */}
          <section style={{ marginBottom: 40 }}>
            <Typography variant="h3" component="h1">
              {project.name}
            </Typography>
            <Typography variant="h5">
              <Link href={`https://www.github.com/${project.repository_name}`}>
                {project.repository_name}
              </Link>
            </Typography>
          </section>

          {/* Languages */}
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: '1fr 1fr 1fr',
              gridTemplateRows: 'auto',
              alignItems: 'center',
              gridGap: 20,
            }}
          >
            {project.languages.map((language) => {
              return (
                <NextLink
                  href={{
                    pathname: '/projects/[id]/[language_code]',
                    query: {
                      id: project.id,
                      language_code: language.language_code,
                    },
                  }}
                >
                  <Card
                    style={{
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      padding: 20,
                    }}
                    key={language.id}
                  >
                    <Typography variant="h6" component="h4">
                      {COUNTRIES[language.language_code]?.flag} {language.name}
                    </Typography>
                  </Card>
                </NextLink>
              )
            })}
          </div>
        </Container>
      </main>
    </div>
  )
}

export default ProjectPage
