import fs from 'node:fs/promises'


async function run() {
    const res = await fetch('https://abdulrahman1s-fiverr-api.deno.dev/abdulrahman1s/reviews')

    if (!res.ok) throw res

    const reviews = await res.json()
    const content = reviews.map((r) => `- ${r.username}: **${r.comment}**`).join('\n')

    console.log(content)
}


run().catch(console.error)
