
export const markerColor = (driverNum:number): string => {
  const colors = ["#C2272D", "#F8931F", "#FFFF01", "#009245", "#0193D9", "#0C04ED", "#612F90", "#752651", "#AB70C0", "#D5739E"];
  
  return colors[driverNum];
};

export const geojsonMarkerOptions = (driverNum?: number | string) => {
  const color = driverNum && markerColor(Number(driverNum))
  return {
    radius: 8,
    fillColor: color || "#752651",
    fillOpacity: 0.6,
    color: 'grey',
    weight: 0.8,
    opacity: 1,
  };
}

