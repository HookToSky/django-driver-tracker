
export const fakeEartquakeData = {
    type: 'FeatureCollection',
    metadata: {
        generated: 1622556930000,
        url: 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson',
        title: 'USGS All Earthquakes, Past Day',
        status: 200,
        api: '1.10.3',
        count: 358
    },
    features: [
        {
            type: 'Feature',
            properties: {
                mag: 2,
                place: '21 km WSW of Akhiok, Alaska',
                time: 1622556547604,
                updated: 1622556761121,
                tz: null,
                url: 'https://earthquake.usgs.gov/earthquakes/eventpage/ak0216zm2rk8',
                detail: 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak0216zm2rk8.geojson',
                felt: null,
                cdi: null,
                mmi: null,
                alert: null,
                status: 'automatic',
                tsunami: 0,
                sig: 62,
                net: 'ak',
                code: '0216zm2rk8',
                ids: ',ak0216zm2rk8,',
                sources: ',ak,',
                types: ',origin,',
                nst: null,
                dmin: null,
                rms: 0.89,
                gap: null,
                magType: 'ml',
                type: 'earthquake',
                title: 'M 2.0 - 21 km WSW of Akhiok, Alaska'
            },
            geometry: {
                type: 'Point',
                coordinates: [-154.5126, 56.8927, 0]
            },
            id: 'ak0216zm2rk8'
        },
        {
            type: 'Feature',
            properties: {
                mag: 0.85,
                place: '7km W of Cobb, CA',
                time: 1622556388240,
                updated: 1622556485751,
                tz: null,
                url: 'https://earthquake.usgs.gov/earthquakes/eventpage/nc73568521',
                detail: 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/nc73568521.geojson',
                felt: null,
                cdi: null,
                mmi: null,
                alert: null,
                status: 'automatic',
                tsunami: 0,
                sig: 11,
                net: 'nc',
                code: '73568521',
                ids: ',nc73568521,',
                sources: ',nc,',
                types: ',nearby-cities,origin,phase-data,',
                nst: 9,
                dmin: 0.007309,
                rms: 0.01,
                gap: 166,
                magType: 'md',
                type: 'earthquake',
                title: 'M 0.9 - 7km W of Cobb, CA'
            },
            geometry: {
                type: 'Point',
                coordinates: [-122.8031693, 38.8283348, 1.46]
            },
            id: 'nc73568521'
        }
    ]
};
