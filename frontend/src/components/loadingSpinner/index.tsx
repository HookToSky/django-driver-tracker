import React, { FC } from 'react';
import loader from './loader.gif';
import styles from './index.module.sass';

const LoadingSpinner: FC = () => {
    return (
        <div data-testid="spinner" className={styles.loader}>
            <img src={loader} alt="loader" />
        </div>
    );
};

export default LoadingSpinner;
